import requests
import random
import sys

cat_url = "https://cat-fact.herokuapp.com/facts"
r = requests.get(cat_url)
r_obj_list = r.json()

fact_list = ["Cats are nutbars", "Cats can exist in five dimensions."]

for fact in r_obj_list:
  fact_list.append(fact["text"])

def select_random_fact(fact_arr):
  return fact_arr[random.randint(0, len(fact_list))]

random_fact = select_random_fact(fact_list)

print(random_fact)

print(f"::set-output name=fact::{random_fact}")