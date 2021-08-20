from icecream import ic
import requests

auth_payload = {
	"apiName": "VTubeStudioPublicAPI",
	"apiVersion": "1.0",
	"requestID": "SomeID",
	"messageType": "AuthenticationTokenRequest",
	"data": {
		"pluginName": "My Cool Plugin",
		"pluginDeveloper": "My Name",
	}
}
# r = ic(requests.get('https://api.github.com/events'))
r = ic(requests.post('http://host.docker.internal:8001/', data = auth_payload))
ic(r.json())