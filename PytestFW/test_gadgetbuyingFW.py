import json
import os
import sys

import pytest



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from POM_GadgetBuying.Buying_login import login_page
from POM_GadgetBuying.vegcart_fresh import vegcart


path='../json/test data.json'
with open (path) as f:
    data_item=json.load(f)
    referlist_name1=data_item["data1"]
    referlist_name2 = data_item["data2"]

@pytest.mark.regression
@pytest.mark.parametrize("refer_name",referlist_name1)
def test_gadget(browserInstance,refer_name):
    driver=browserInstance
    ll=login_page(driver)
    ll.title()
    cart=ll.login(refer_name["username"],refer_name["password"])
    cart.title()
    check=cart.cart_logic(refer_name["label"])
    check.title()
    submit=check.checkout_logic()
    submit.title()
    shopcheck=submit.submit_logic(refer_name["country"])
    shopcheck.title()
    shopcheck.shop_logic(refer_name["name"],refer_name["email"],refer_name["pwd"],refer_name["date"])

@pytest.mark.regression
@pytest.mark.parametrize("listing",referlist_name2)
def test_vegfresh(checkinstance,listing):
    driver=checkinstance
    vc= vegcart(driver)
    vc.vegsearch(listing["value"])
    vc.vegcarting()
    st=vc.cartoption()
    st.summation()
    st.message(listing["invalid_promo_name"],listing["valid_promo_name"])
    st.cal()


