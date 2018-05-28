[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **FVCcall_API** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: FVCcall_API

Published in: Face Value of Companies

Description: "Calls Emotion API of Microsoft Cognitive Service. Requires either a key from Microsoft Azure (www.azure.microsoft.com). Can be used to send images from hard drive to API, returns a vector of eight emotion-scores."


Keywords: 'neural-network, estimation, empirical, optimization, descending-gradients'

Author: Sophie Burgard

Submitted: '21.11.2017'



```

### PYTHON Code
```python



def call_emotion_api(source):

    import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json

    #define dictionary
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        #data: must contain binary vector of picture
        'Content-Type': 'application/octet-stream',
        #'Content-Type': 'application/json', #alternative for URL's
        #AZURE KEY:
        'Ocp-Apim-Subscription-Key': 'XXXXXXXXX', #insert subscription key
    }
    
    #params: if face rectangles are provided by user
    params = urllib.parse.urlencode({
    })
    
   
    try:    
        body = open(source, "rb").read()
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read() 
        #print(data)
        conn.close()
        #return json.loads(data.decode('utf8'))
        return data.decode('utf8')
    except Exception as e:
        print(e.args)
        return(e.args)

```

automatically created on 2018-05-28