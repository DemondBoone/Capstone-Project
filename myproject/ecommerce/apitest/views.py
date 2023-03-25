import base64
import requests
from django.http import JsonResponse #this will allow me to send stuff in json
from django.shortcuts import render


# Add the get_ebay_oauth_access_token function, this will be what gets my oauth access token, remember the differences between the oatuh token and the regular token, there are also two different modes
def get_ebay_oauth_access_token(client_id, client_secret, is_sandbox=True):
    base_url = 'https://api.sandbox.ebay.com' if is_sandbox else 'https://api.ebay.com' #because im in sandbox but needed to swith to productions
    url = f'{base_url}/identity/v1/oauth2/token'

    credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8') #encoding for my credentials
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {credentials}',
    }
    data = {
        'grant_type': 'client_credentials',
        'scope': 'https://api.ebay.com/oauth/api_scope', #ebay api, scope using my oauth, its pretty much what is needed to ask access
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f'Error obtaining access token: {response.text}')

# I Updated 03/21/23 the test_ebay_api view
def test_ebay_api(request):
    client_id = 'DemondBo-projectc-PRD-2cd640c06-af32d4fb'
    client_secret = 'PRD-cd640c06271b-44a0-4484-9cca-8f4d'
    is_sandbox = False #this is currently in produciton mode, this is my traffic jam as i couldnt find a way to sell my own thing in sandbox api, therefore I could get my own personnel things to sell in neither sandbox or production

    access_token = get_ebay_oauth_access_token(client_id, client_secret, is_sandbox) #threee parameters here
    base_url = 'https://api.sandbox.ebay.com' if is_sandbox else 'https://api.ebay.com'

    url = f'{base_url}/buy/browse/v1/item_summary/search'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'X-EBAY-C-ENDUSERCTX': 'affiliateCampaignId=ePNCampaignId,contextualLocation=country=US,zip=95125'
    }
    params = { #03/24/2023 I need to change this!!!!!!!!!
        'q': 'laptop',
        'limit': '10',
    }


#i have collected the json from my response
    response = requests.get(url, headers=headers, params=params)
    data = response.json() #parsed my data, ive actually saw the json data for and ideo on information
    laptops = data.get('itemSummaries', [])[:5]  # extract the five lines, which is causing it randomly this will Extract the first 5 laptops from the response/ dont forget to change the variable
    return render(request, 'laptops.html', {'laptops': laptops}) #try this code if failed 



# import base64
# import requests
# from django.http import JsonResponse





    # url = f'{base_url}/buy/browse/v1/item_summary/search'
    # headers = {
    #     'Authorization': f'Bearer {access_token}',
    #     'Content-Type': 'application/json',
    #     'X-EBAY-C-ENDUSERCTX': 'affiliateCampaignId=ePNCampaignId,contextualLocation=country=US,zip=95125'
    # }
    # params = {
    #     'q': 'laptop',
    #     'limit': '10',
    # }

    # response = requests.get(url, headers=headers, params=params)
    # data = response.json()

    # return JsonResponse(data)
    # this is what I previously used to test my api to see if worked and it successfully worked