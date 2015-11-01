import bottle
from bottle import Bottle, route, request, response, run, get, post, redirect
import odoorpc
from odoorpc import rpc
import json
import string

class EnableCors(object):
    name = 'enable_cors'
    api = 2

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

            if bottle.request.method != 'OPTIONS':
                # actual request; reply with the actual response
                return fn(*args, **kwargs)

        return _enable_cors
        
app = bottle.app()

user = ''
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login('demo','admin','admin')
user = odoo.env.user


@bottle.route('/users', method='GET')
def users():
    data = []
    Users = odoo.env['res.users']
    user_ids = Users.search([])
    for user in Users.browse(user_ids):
        data.extend([{'nombre':user.name,'id':user.id, 'activo':user.active}])
    return json.dumps(data)

@bottle.route('/customers', method='GET')
def customers():
    data = []
    Customers = odoo.env['res.partner']
    customer_ids = Customers.search([])
    for customer in Customers.browse(customer_ids):
        data.extend([{'nombre':customer.name,'id':customer.id}])
    return json.dumps(data)

@bottle.route('/orders', method='GET')
def orders():
    data = []
    Orders = odoo.env['sale.order']
    order_ids = Orders.search([])
    for order in Orders.browse(order_ids):
        data.extend([
            {
                'id':order.id,
                'date_order': str(order.date_order),
                'amount_total':order.amount_total
            }])
    return json.dumps(data)

@bottle.route('/invoices', method='GET')
def invoices():
    data = []
    Invoices = odoo.env['account.invoice']
    invoice_ids = Invoices.search([])
    for invoice in Invoices.browse(invoice_ids):
        data.extend([
            {
                'id':invoice.id,
            }])

    return json.dumps(data)

@bottle.route('/products', method='GET')
def products():
    data = []
    Products = odoo.env['product.template']
    product_ids = Products.search([])
    for product in Products.browse(product_ids):
        data.extend([
            {
                'id':product.id,
                'name':product.name,
            }])

    return json.dumps(data)

@bottle.route('/user/<idu>', method='GET')
def user(idu):
    Users = odoo.env['res.users']
    user = Users.browse([int(idu)])
    img = user.image
    if img:
        i = img.encode('ascii', 'ignore')
    else:
        i = "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"
    data = json.dumps({
        'nombre':user.name,
        'id':user.id,
        'image':i,
    })
    return json.loads(json.dumps(data))

@bottle.route('/customer/<idu>', method='GET')
def customer(idu):
        Customers = odoo.env['res.partner']
        customer = Customers.browse([int(idu)])
        img = customer.image
        if img:
            i = img.encode('ascii', 'ignore')
        else:
            i = "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"
        data = json.dumps({
            'nombre':customer.name,
            'id':customer.id,
            'image':i,
            'email':customer.email,
            'phone':customer.phone,
            'street':customer.street,
            'city':customer.city,
            'zip':customer.zip,
            'website':customer.website,
            'contact_email':customer.child_ids.email,
            'contact_name':customer.child_ids.name,
        })
        return json.loads(json.dumps(data))

@bottle.route('/order/<idu>', method='GET')
def order(idu):
    data = []
    Orders = odoo.env['sale.order']
    order = Orders.browse([int(idu)])

    for line in order.order_line:
        data.extend([{
            'id':line.id,
            'product':line.name,
            'product_uom_qty':line.product_uom_qty,
            'price_unit':line.price_unit,
        }])

    order_detail = json.loads(json.dumps({'order_id':order.id, 'order_date':str(order.date_order), 'order_name':order.name}))
    pedido = {'lineas':data,'order_detail':order_detail}
    print "order"
    return json.dumps(pedido)

@bottle.route('/create_order', method='POST')
def create_order():
    customer = request.forms.customer_id
    product = request.forms.product_id

    Orders = odoo.env['sale.order']
    order_id = Orders.create({'partner_id':int(customer)})

    # Redirect to view current order
    bottle.redirect('http://localhost:8100/#/app/order/'+str(order_id))
    return order_id


@bottle.route('/invoice/<idu>', method='GET')
def invoice(idu):
    data = []
    Invoices = odoo.env['account.invoice']

    invoice = Invoices.browse([int(idu)])

    for line in invoice.invoice_line:
        data.extend([{
            'id':line.id, 'product':line.name
        }])

    invoice_detail = json.loads(json.dumps({'invoice_id':invoice.id, 'invoice_name':invoice.name, 'invoice_number':invoice.number}))
    pedido = {'lineas':data,'invoice_detail':invoice_detail}
    return json.dumps(pedido)

@bottle.route('/product/<idu>', method='GET')
def product(idu):
    data = []
    Products = odoo.env['product.template']
    product = Products.browse([int(idu)])

    img = product.image
    if img:
        i = img.encode('ascii', 'ignore')
    else:
        i = "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"
    data = json.dumps({
        'nombre':product.name,
        'id':product.id,
        'image':i,
        'price':product.list_price,
        'type': product.type,
    })

    return json.loads(json.dumps(data))


app.install(EnableCors())
app.run(host='localhost', port=8080)
