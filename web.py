from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>LAPTOP STORE!!</title>
    </head>
    <body style="color : white" bgcolor="black">
        <table border="1">
            <tr>
                <th>S.NO</th>
                <th>DEVICE_TYPE</th>
                <th>DEVICE_MODEL</th>
                <th>DEVICE_SPECS</th>
                <th>PRICE</th>
                <th>BUY_DETAILS</th>
            </tr>
            <tr>
                <td>1</td>
                <td>LAPTOP</td>
                <td>ASUS TUF A15</td>
                <td>ASUS TUF A15 (2026),Smartchoice,AMD Ryzen 7 8845HS,RTX 3050,16GB RAM (Upgradeable Upto 64GB),512GB SSD,FHD,15.6"(39.6 cm),Win 11,M365 Basic(1Y),Office 24,Black,2.3 Kg,FA506NCG-HN192WS,Gaming Laptop</td>
                <td>₹1,04,990</td>
                <td><a href="https://www.amazon.in/dp/B0H25X3W7F?_encoding=UTF8">BUY_LINK
                </a></td>
            </tr>
                <td>2</td>
                <td>LAPTOP</td>
                <td>HP VICTUS 15</td>
                <td>HP Victus 15 Smartchoice, Intel Core i7-13620H, 6GB RTX 4050, 16GB DDR4, 512GB SSD, FHD, IPS, 144Hz, 300 nits, 15.6''/39.6cm, Win11, Office24, Blue, 2.3kg, fa2805TX/2103, Xbox Gamepass* Gaming Laptop</td>
                <td>₹1,38,490</td>
                <td><a href="https://www.amazon.in/dp/B0HK85ZRZ9?_encoding=UTF8">BUY_LINK
                </a></td>         
            <tr>
                <td>3</td>
                <td>LAPTOP</td>
                <td>DELL ALIENWARE 15</td>
                <td>Dell Alienware 15 Gaming Laptop, AMD Ryzen R7 260 Processor, NVIDIA GeForce RTX 5050 8 GB GDDR7, 16GB:512GB SSD, 15.3" WUXGA 165Hz 300 nits Display, Alienware Backlit Keyboard, Win 11 + MSO'24, 2.25kg</td>
                <td>₹1,50,990</td>
                <td><a href="https://www.amazon.in/dp/B0H9XM7K3Z?_encoding=UTF8">BUY_LINK
                </a></td>

            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self): 
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()