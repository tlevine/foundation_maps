import requests
from vlermv import cache #, transformers, serializers

#@cache('~/.foundation_maps/cookie', key_transformer = transformers.magic)
def cookie(_):
    raise NotImplementedError('You must obtain the cookies manually.')
    return requests.head('https://maps.foundationcenter.org')

#@cache('~/.foundation_maps/getList', key_transformer = transformers.identity_str)
@cache('~/.foundation_maps/getList')
def getList(cookie):
    url = 'https://maps.foundationcenter.org/web_services/getList.php'
    params = {
        'view': 'fm-view-list',
        'subjects': 'all',
        'popgroups': 'all',
        'years': 'all',
        'location': '6295630',
        'geoScale': 'ADM0',
        'layer': 'recip',
        'boundingBox': '-135,20.3034175184893,-41.1328125,58.99531118795094',
        'gmOrgs': 'all',
        'recipOrgs': 'all',
        'tags': 'all',
        'keywords': '',
        'pathwaysOrg': '',
        'pathwaysType': '',
        'acct': 'aecf',
        'typesOfSupport': 'all',
        'amtRanges': '3,4',
        'gmTypes': 'all',
        'andOr': '0',
        'custom': 'all',
        'customArea': 'all',
        'listType': 'recip',
        'listType': 'recip',
        'sortColumn': 'amount',
        'sortOrder': 'desc',
    }
    headers = {
        'Cookie': cookie,
    }
    return requests.get(url, params = params, headers = headers)

@cache('~/.foundation_maps/getOrganizationProfile')
def getOrganizationProfile(org_key, cookie = None):
    url = 'https://maps.foundationcenter.org/web_services/getOrganizationProfile.php'
    params = {
        'org_key': org_key,
        'type': 'ein',
    }
    headers = {
        'cookie': cookie,
    }
    return requests.get(url, params = params)
