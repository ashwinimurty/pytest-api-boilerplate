import pytest, json
from src.character_model import CharacterEP
import requests

get_obj = CharacterEP()
    
def test_character_endpoint():
    """
        Test Purpose: Test the character endpoint returns all characters
    """ 
    req = get_obj.get().build_request()
    resp = get_obj.last_get
    out = json.loads(resp.text)
    print("All the characters output is", json.loads(resp.text))
    ids = []
    for ele in out['results']:
        ids.append(ele['id'])
    print("ALL IDS", ids)
    #assert based on the number of ids or the values of the ids itself
    assert len(ids) == 20


def test_single_character_endpoint():
    """
       Test Purpose: Test the character endpoint returns a single character
    """
    #Using the input id 2
    req = get_obj.get(2).build_request()
    resp = get_obj.last_get
    out = json.loads(resp.text)
    print("Output for single character is", out)
    if out['id'] == 2:
        print("Match")
    assert out['id'] == 2


def test_multiple_characters():
    """
        Test Purpose: Test the character endpoint returns multiple characters
    """
    #using the input ids 1 and 3
    req = get_obj.get([1,3]).build_request()
    resp = get_obj.last_get
    out = json.loads(resp.text)
    print("Output for multiple character is", out)
    #print("First ID",out[0]['id'])
    #print("Second ID",out[1]['id'])
    assert out[0]['id'] == 1 and  out[1]['id'] == 3
