from flask import Flask, request, make_response
app = Flask(__name__)

#from OpenSSL import SSL
#context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
#context.use_privatekey_file('localhost.key')
#context.use_certificate_file('localhost.crt') 


@app.route('/')
def index():
    content = "It's easier to ask forgiveness than it is to get permission."
    fwd_for = "X-Forwarded-For: {}".format(
        request.headers.get('x-forwarded-for', request.remote_addr)
    )
    real_ip = "X-Real-IP: {}".format(
        request.headers.get('x-real-ip', request.remote_addr)
    )
    fwd_proto = "X-Forwarded-Proto: {}".format(
        request.headers.get('x-forwarded-proto', request.scheme)
    )

    output = "\n".join([content, fwd_for, real_ip, fwd_proto])
    response = make_response(output, 200)
    response.headers["Content-Type"] = "text/plain"

    return response

   # connection = http.client.HTTPSConnection("httpbin.org")
   # connection.request("GET", "/get")

   # response = connection.getresponse()
   # print(response.status)


if __name__ == ("__main__"):
    #context = ('localhost.crt', 'localhost.key')

    #app.run(debug=True, ssl_context=context)

# app.run(ssl_context=('cert.pem', 'key.pem'))
    #context = ('localhost.crt', 'localhost.key') #if __name__ == ("__main__"):

    #app.run(host='0.0.0.0', port = 8000, debug=True, ssl_context\'C:\Users\rendo\Desktop\my_projectadhoc\ssl\key.pem=context)

    app.run(host='0.0.0.0', port = 8000)