# -*- coding: utf-8 -*-
"""ac3_intro_to_jinja

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qrl9WZ9y3ryrrV3BnDP4w65MfOlBth3R

# AutoCon3 Introduction to jinja
"""

# pip install jinja2

"""jinja2 already available in colab environment"""

tmp_str = "I am in {{ city }}"
tmp_str3 = "I am in {{ payload['city'] }}"

import jinja2 as j2

t = j2.Template(tmp_str)

result = t.render(city="Denver")
print(result)

mydict = {"city": "Los Angeles"}

result2 = t.render(mydict)
print(result2)

t = j2.Template(tmp_str)
result3 = t.render(payload=mydict)
print(result3)

t3 = j2.Template(tmp_str3)
result4 = t3.render(payload=mydict)
print(result4)



