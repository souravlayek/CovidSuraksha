from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import _get_queryset
from .models import  Shop,ItemQuerry
from accounts.models import ShopManagerProfile
from django.contrib.auth.decorators import login_required
from .forms import NewShopForm,ItemQuerryForm,AppoinmentForm
from accounts.models import DoctorProfile,ShopManagerProfile,UserProfile
from django.db.models import Q

profilemodel =  {'doctor':DoctorProfile,'user':UserProfile,'shopmanager':ShopManagerProfile}

def get_object_or_notfound(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.filter(*args, **kwargs)
    except:
        return False

class UserPermissionMixin:
    allowed = ['shopmanager']
    def dispatch(self, request, *args, **kwargs):
        if not request.user.usertyp in  self.allowed:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
@login_required
def OwnerShops(request):
    owner = get_object_or_404(ShopManagerProfile, user=request.user)
    shops = get_object_or_notfound(Shop ,owner=owner)
    # pending_context = {}
    # for i in shops:
    #     itemquerry = get_object_or_notfound(ItemQuerry, shop=i)
    #     pendingquerry = len(itemquerry.filter(pending=True))
    #     pending_context[i.name +'pending'] == pendingquerry

    return render(request, 'shop/ownerhome.html', {'shops':shops})

def AddShop(request):
    if request.method == 'POST':
        owner = get_object_or_404(ShopManagerProfile, user=request.user)
        forms = NewShopForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.owner = owner
            instances.save()
            return redirect('shop:ownerview')
    else:
        form = NewShopForm
        return render(request, 'shop/addshop.html', {'form':form})

def ShopUserHome(request):
    profile = profilemodel[request.user.usertype]
    user = get_object_or_404(profile, user=request.user)
    shop = get_object_or_notfound(Shop, district = user.district)
    return render(request, 'shop/userhome.html',{'shops':shop})


def itemqueryview(request,id):
    shop = get_object_or_404(Shop, id=id)
    itemquerry = get_object_or_notfound(ItemQuerry, shop=shop)
    appoinment = _get_queryset(ItemQuerry)
    print(appoinment)
    if request.method == 'POST':
        forms = ItemQuerryForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            instances.shop = shop
            instances.save()
            shop_instances = shop
            shop_instances.pendingitems = len(itemquerry.filter(pending = True))
            shop_instances.save()
            return redirect('shop:inshop', id=id)
    else:
        appoinmentform = AppoinmentForm
        form = ItemQuerryForm
        return render(request, 'shop/inshop.html', {'form':form,'shop':shop,'itemquerry':itemquerry,'appoinmentform':appoinmentform,'apps':appoinment})

def appoinmentview(request,id):
    if request.method == 'POST':
        item = get_object_or_404(ItemQuerry, id=id)
        forms = AppoinmentForm
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            instances = form.save(commit=False)
            item_inastances = item
            item_inastances.pending = False
            item_inastances.approved = True
            item_inastances.appoinment = instances.appoinment
            item_inastances.notes = instances.notes
            item_inastances.save()
            shop = get_object_or_404(Shop, pk=item.shop.id)
            itemquerry = get_object_or_notfound(ItemQuerry, shop=shop)
            shop_instances = shop
            shop_instances.pendingitems = len(itemquerry.filter(pending = True))
            shop_instances.save()
            return redirect('shop:inshop',item.shop.id)

def search(request):
    if request.GET:
        profile = profilemodel[request.user.usertype]
        user = get_object_or_404(profile, user=request.user)
        shop = get_object_or_notfound(Shop, district = user.district)
        search_term = request.GET['search_term']
        search_results = shop.filter(
            Q(name__icontains=search_term) |
            Q(shoptype__icontains=search_term) |
            Q(town__iexact=search_term)
        )
    return render(request, 'shop/userhome.html',{'shops':search_results})