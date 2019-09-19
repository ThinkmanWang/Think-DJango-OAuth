import requests

ret = requests.post("http://localhost:8000/api/fxxk-plus/123"
                    , headers={"Authorization": "Bearer HxW4UUDaq6Hibafrs5aPNVk4uUpPR7"}
                    )

print(ret.status_code)
print(ret.text)