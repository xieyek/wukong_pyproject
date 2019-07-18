
# 环境配置：0-urgent、1-big、2-h5、3-finance、4-spare、5-adminv1、6-reserve、7-hotfix
first_url = 1
# 数据库配置
host="wukong-php-test.rwlb.rds.aliyuncs.com"
db="wukong_urgent"
port=3306
user = "dengbingqiu"
passwd = "dengbingqiu123$@#76"
# 已经注册过的代理
recommend_mobile = "19990984813"
# 测试机的openid
#openid='eyJpdiI6InBGdkQ1N3d6TzAzclB0dDZaa2VYSXc9PSIsInZhbHVlIjoiZm54YmNIQWRoU09BV1BqMFZncnpza1MxeU9BUElVVzl2eGpLNnJWNElXcUxUTVFLallLaTJEQk52M0I4cGtiYiIsIm1hYyI6IjM4ODZhNTkxODg3MGI1MWM1NjYwYjVlNDA2ODZiMGVkYWJiNTcxZjVmN2IyZmViOTQwMWViNzJmYzJkZWFmMGEifQ==',
openid = "eyJpdiI6IkVWSUhvMUJEamJ5bHBTTDF6WTQwUlE9PSIsInZhbHVlIjoiZVwvRVl4aEFPaERZZmt4eVcwV2Z4eVRQaFRcLytrT0VXUGtUVGt5ZFhZcmFKdGpYU1Z3eVhVeWRCWHNvZWs3YWxuIiwibWFjIjoiMTdhZTM1NjQwZmExMDIwYTk0NTNkODg5MGRkNWFiMDdmZTA3ZGQyNDI1MmViMjNiN2E5NGU5OTFhZTg0MjYwNiJ9"
# 未注册的电话
# no_register_mobile = "199"+ Common.random_num(8)
# 接收全球合伙人的短信电话
operation_mobile = "13725321096"
# 运营者token
#operation_token1 是管理员
operation_token1='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9iaWcuc2h1aXhpb25na2VqaS5uZXRcL2FkbWluXC9BZG1pbkxvZ2luIiwiaWF0IjoxNTYzNDU1ODE2LCJleHAiOjE1NjQ2NjU0MTYsIm5iZiI6MTU2MzQ1NTgxNiwianRpIjoiZ2FLOWZuSzNOQ09HckoxViIsInN1YiI6MSwicHJ2IjoiOTcwMzBiM2RiMjQyMDhjNDJkZTcyZmY2NTZjNDcwYWIyMDJmYjlmMCIsInJvbGUiOiJBRE1JTiIsInVzZXJuYW1lIjoic3hraiIsImlkIjoxLCJpc19hZG1pbiI6dHJ1ZSwicm9sZV9pZCI6MSwicmVzZXRfdGltZSI6IjIwMTktMDQtMjcgMjI6NDQ6NDMifQ.L_WRsPACFSjn_Da8XDzqzVxCDd6nFUVYtUO8Dv9gnNk'
#下面是创建的后台角色
operation_token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9iaWcuc2h1aXhpb25na2VqaS5uZXRcL2FkbWluXC9BZG1pbkxvZ2luIiwiaWF0IjoxNTYzNDUzODMyLCJleHAiOjE1NjQ2NjM0MzIsIm5iZiI6MTU2MzQ1MzgzMiwianRpIjoiRERzSXQ3Z0dnQ09CaUV1RiIsInN1YiI6ODcsInBydiI6Ijk3MDMwYjNkYjI0MjA4YzQyZGU3MmZmNjU2YzQ3MGFiMjAyZmI5ZjAiLCJyb2xlIjoic2hvdWhvdSIsInVzZXJuYW1lIjoiMTgwMDAwMDA0MTciLCJpZCI6ODcsImlzX2FkbWluIjp0cnVlLCJyb2xlX2lkIjoyNSwicmVzZXRfdGltZSI6IjIwMTktMDctMTUgMTU6MDk6MjcifQ.wRqokWjpMfiAdoxD_bRKMuUSkhWHEptX_h8-fTMXXc0'
# 供应商的token
supplier_token ='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9iaWcuc2h1aXhpb25na2VqaS5uZXRcL3NlbGxlclwvTG9naW4iLCJpYXQiOjE1NjMzNzM3MTEsImV4cCI6MTU2NDU4MzMxMSwibmJmIjoxNTYzMzczNzExLCJqdGkiOiJwM1pwWm9DMmJPc3I1d1JZIiwic3ViIjo1OTMsInBydiI6IjQ4NTA2NTc3M2QxNTAzNGQ0MjU1YWY2MzQwMzFhNGQyYzQyYTU1NGUiLCJpZCI6NTkzLCJyb2xlIjoiQlVTSU5FU1MiLCJhY2NvdW50X2lkIjo1NTQsInJlc2V0X3RpbWUiOm51bGwsInJvbGVfaWQiOjU1NCwiaXNfYnVzaW5lc3MiOnRydWUsImJ1c2luZXNzX2lkIjo1OTN9.Nyt7FOl0fqStYhWbdKZWqJsxwYd9k6hUuo1JQdtvOjk'
supplier_token1 = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYmlnLnNodWl4aW9uZ2tlamkubmV0XC9CdXNpbmVzc0F1dGhzIiwiaWF0IjoxNTU0NzA2NzM5LCJleHAiOjE1NTU5MTYzMzksIm5iZiI6MTU1NDcwNjczOSwianRpIjoicnNYSm5tQ1cwdThrZjRVZiIsInN1YiI6MywicHJ2IjoiNDg1MDY1NzczZDE1MDM0ZDQyNTVhZjYzNDAzMWE0ZDJjNDJhNTU0ZSIsImlkIjozLCJyb2xlIjoiQlVTSU5FU1MiLCJhY2NvdW50X2lkIjozLCJyZXNldF90aW1lIjpudWxsLCJyb2xlX2lkIjo0LCJpc19idXNpbmVzcyI6dHJ1ZX0.h33gXA-YdRTMOt5gc9JYF7pM8L2qUdx-0QVKAX88IYk"
# 掌柜的token
shopkeeper_token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9iaWcuc2h1aXhpb25na2VqaS5uZXRcL2FwcFwvTG9naW5CeUg1IiwiaWF0IjoxNTYzNDM3MzkzLCJleHAiOjE1NjQwNDIxOTMsIm5iZiI6MTU2MzQzNzM5MywianRpIjoiN2k5bzRCOEtyaTdKMXh3byIsInN1YiI6NjA5MzAsInBydiI6IjZkOWJkZjNhOTA1NzZhN2E2MmY4Y2M1ZDJjNWJiNmY4ZWFjYWQ4MTciLCJpZCI6NjA5MzAsInJvbGUiOiJVU0VSIiwiaXNfdXNlciI6dHJ1ZSwicm9sZV9pZCI6MCwicmVzZXRfdGltZSI6IjIwMTktMDctMTUgMTM6Mzk6MzEifQ.Sqjp0b47jqcuDp8PTaiVklO-S2ZyLInvjOV6T02bMac'
