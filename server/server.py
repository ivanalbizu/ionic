import web
from web import form
import odoorpc
from odoorpc import rpc
import json
import string

'''
http://pythonhosted.org/OdooRPC/tuto_browse_methods.html
https://github.com/osiell/odoorpc/blob/master/odoorpc/tests/test_model.py
'''

urls = (
    '/',                'index',
    '/users',           'users',
    '/user/(.+)',       'user',
    '/customers',       'customers',
    '/customer/(.+)',   'customer',
    '/orders',          'orders',
    '/create_order',    'create_order',
    '/order/(.+)',      'order',
    '/invoices',        'invoices',
    '/invoice/(.+)',    'invoice',
    '/products',        'products',
    '/product/(.+)',    'product',
    '/testedit/(.+)',    'testedit',
)
#postgresql://admingkjiqmy:l5BXAQ4892et@127.7.171.130:5432
hostname = 'localhost'
username = 'admingkjiqmy'
password = 'l5BXAQ4892et'
database = 'myodoo'


user = ''
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login('demo','admin','admin')
user = odoo.env.user

'''
odoo = odoorpc.ODOO('postgresql://admingkjiqmy:l5BXAQ4892et@127.7.171.130:5432')
odoo.login('odooV1610','admin','admin')
user = odoo.env.user
'''
#cnt = rpc.ConnectorJSONRPC('127.7.171.130', port=5432)
#cnt.proxy_json.web.session.authenticate(db='myodoo',login='admingkjiqmy',password='l5BXAQ4892et')

class testedit(object):
    def POST(self):
        data = web.input()
        test = data.algo

class index:
    def GET(self):
        return type(user.name+user.company_id.name)
#data = [ { 'dateTime':str(now), 'random':rand} ]

class users:
    def GET(self):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')
        Users = odoo.env['res.users']
        user_ids = Users.search([])
        for user in Users.browse(user_ids):
            data.extend([{'nombre':user.name,'id':user.id, 'activo':user.active}])
        return json.dumps(data)

class user:
    def GET(self, idu):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')

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


class customers:
    def GET(self):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')
        Customers = odoo.env['res.partner']
        customer_ids = Customers.search([])
        for customer in Customers.browse(customer_ids):
            data.extend([{'nombre':customer.name,'id':customer.id}])
        return json.dumps(data)

class customer:
    def GET(self, idu):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')

        Customers = odoo.env['res.partner']
        customer = Customers.browse([int(idu)])
        img = customer.image
        if img:
            i = img.encode('ascii', 'ignore')
        else:
            i = "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAHNUlEQVR4Xu2dV6hkRRCGvzWjK4g5YI4vRsw5o2LChA9GUFDBgOlBDGACA4qiCIYHQcUEImbFnBNmxYAi+qAi5pz53Z51V/e6OztTfapOV8PlsuxMdfVf3/Sd011dPYlsTSswqenR5+BJABqHIAFIABpXoPHh5wyQADSuQOPDzxkgAWhcgcaHnzNAAtC4Ao0PP2eABKBxBRoffs4ACUDjCjQ+/JwBEoDGFWh8+DkDJACNK9D48HMGSAAaV6Dx4bc0A8wJrAWsCawGLA5MLvH/DvgMeAd4tfz80QIbfQdgbmAn4ABgR2ChWQzql8D9wHXAfcCvs/i+cC/rKwDzA4cDJwHLjBiVj4ALgKuBH0e05e7tfQRgd+BSYPkxq/0BcDRw15jtdmquTwAsAFwGHGKsqGaCY/oyG/QFgKWBe8qXPOP4/23+JWAX4JManVn20QcAVgIeMpjyZ6a7/iRsA3w4sxd6/v/oACwBPAms3JHIemzcDPi8o/5H7jYyAHrEexTYZGQVRjPwGLAd8NtoZrp5d2QAzgNO7ka2//R6FnC6E1+GciMqAOsBzwNzDDVauxf/DqwDvG7XhY3liADIZ/3d73rq/3dEHga2tQmTndWIAGwPPGAnyUiWtwQeH8lC5TdHBEBr81rX99juALQSGaZFA0Dr+lqb9+q3vgtoUUo7iyGaVyEnEu844GLnyh4FXOHcx6nuRQNAU+yuzsW9FdjXuY8hARCsXwyxp99VDD4Fluyq82H7jTQDaNk3yubLwoCSSty3SABsWp7/3YsKbFgWqtz7GgkAbb9GScbQY6rXtYrpoIwEgL5Y3ez+IzXFwb2A2yL4GgkALbDcHkHUkiyiBBX3LRIASr5Q4keEtgXwRARHIwGgpI/3IogKLFdWLN27GwkAHez4AZjHuarycUEgxMGSSAAo7k8DGzsH4JGSK+jczSnuRQPgHOAU58qeAZzp3Mep7kUDYAPgOefirl3OFjp3M+YMIGDfBNZwqq4OlgqAMC3aDCBhtd16uVOFDwOucerbDN2KCMB8gA5leNtxU6LKKsAvCYC9AgcB19p3M1QP+wM3DfUOBy+OOAMMnl4edPS4pVoCqkPwp4OYDuVCVAA0SOUHvgwsOtSIx/9iJYDoTECUXIXpFIgMgAai/YF7O1wd/BnYIVoq+LQERAdAY9E28Y0dnBJSBrD6DrHtO9HE1wcANLY9CgR6QqjRVCpGwY+SoDKhJn0BQANUGpa+ha9gTMD7wH7Ai8b9VDHfJwAkmKqAXQQcaqSeysOcCHxtZL+62b4BMBBQRRvOBrYek6J65DwVeGZM9tyY6SsAA4GVSazl2X3KHv0wwn8D6JDHVX0M/ECIvgMwGKe+HOo4uR4bVS10dWCxaaD4tpznext4raSe6dP+0zDERHxtKwBEjE0VnxOAKjL77SQB8BubKp4lAFVk9ttJAuA3NlU8SwCqyOy3kwTAb2yqeJYAVJHZbycJgN/YVPEsAagis99OWgFgXkAlZnSphH50pczgt8rN6k4g/ehc31flR6le+nevW98AWBXYqBwcWbHkBui3UshnZ6za9v0YeBfQPsEb5bKItwBlBIVvsyOKl0Hrk6sNHpWOVdCVELJIJeeUEfQsoFLxKgWjQ6shgYgGgKZyJWHuCexW7v6rFPP/7UZ/Nu4GbilX1yhZNESLAoC2b48EDg5QJ1Aw3ABcCbzinQLvAOhTrvKw4cqwl8DrRpMLgTu9guAVAJVZU0qXjoP3oemWsdM8ZhF7A0DZOrr0cas+RH0GY1D1kGM91Q/wAoCey1VZ43hgrp4GfzAsPS1cUmaEztcZPACgRzld0qz7/1pqqnh2YNcJp10CoL6VY39uA5/6icDWVXNKNz+/q5PFXQGgZdjry5Gulj71E41V5ws1G3xfW4wuAFiqPBbp6rds/yigo+471z5mXhuAru75jQKaSt/oFlL9rtJqAqDg6zFo2Soji9uJag3pMbgKBLUA0E1a2jBRDd1sM1dAwdexNvOqIzUAmFwqaKiMSrZZV0Crh5tb5yTUAEDfcLV7l214BbS7qFoEZs0agBPKZojZABowrM0wrRyaNEsANOUracJ7eXcTYcdoVLkF61vdTG4FgGr763r3dccoRMumXihZT2O/g8AKgCMiXZ8ahCyTOsRWAKiyxt5BhI3ipgpgqRztWFsCMFY5TY0lAKby+jeeAPiPkamHCYCpvP6NJwD+Y2TqYQJgKq9/4wmA/xiZepgAmMrr33gC4D9Gph6GAkA7WN6veDWNloHxp8qhmbGatloJHKuTacxOgQTATtsQlhOAEGGyczIBsNM2hOUEIESY7JxMAOy0DWE5AQgRJjsnEwA7bUNYTgBChMnOyQTATtsQlhOAEGGyczIBsNM2hOUEIESY7JxMAOy0DWE5AQgRJjsnEwA7bUNYTgBChMnOyQTATtsQlhOAEGGyczIBsNM2hOUEIESY7Jz8C/303oGx4zx1AAAAAElFTkSuQmCC"
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


class orders:
    def GET(self):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')
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


class order:
    def GET(self, idu):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')

        Orders = odoo.env['sale.order']
        order = Orders.browse([int(idu)])

        for line in order.order_line:
            data.extend([{
                'id':line.id, 'product':line.name
            }])

        order_detail = json.loads(json.dumps({'order_id':order.id, 'order_date':str(order.date_order), 'order_name':order.name}))
        pedido = {'lineas':data,'order_detail':order_detail}
        return json.dumps(pedido)

class create_order:
    '''
    def GET(self):
        form = myform()
        return render.formtest(form)
    '''
    def POST(self):
        #form = myform()
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')
        data = form['test'].value
        data2 = web.input()
        data3 = web.input(id=[])
        print type(data3)
        Orders = odoo.env['sale.order']
        Orders.create({'partner_id':6})
        '''
        User = odoo.env['res.users']
        User.write({'name': "Demo Portal User"})
        '''
        return True


class invoices:
    def GET(self):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')
        Invoices = odoo.env['account.invoice']
        invoice_ids = Invoices.search([])
        for invoice in Invoices.browse(invoice_ids):
            data.extend([
                {
                    'id':invoice.id,
                }])

        return json.dumps(data)


class invoice:
    def GET(self, idu):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')

        Invoices = odoo.env['account.invoice']

        invoice = Invoices.browse([int(idu)])

        for line in invoice.invoice_line:
            data.extend([{
                'id':line.id, 'product':line.name
            }])

        invoice_detail = json.loads(json.dumps({'invoice_id':invoice.id, 'invoice_name':invoice.name, 'invoice_number':invoice.number}))
        pedido = {'lineas':data,'invoice_detail':invoice_detail}
        return json.dumps(pedido)


class products:
    def GET(self):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')
        Products = odoo.env['product.template']
        product_ids = Products.search([])
        for product in Products.browse(product_ids):
            data.extend([
                {
                    'id':product.id,
                    'name':product.name,
                }])

        return json.dumps(data)


class product:
    def GET(self, idu):
        data = []
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('Content-Type', 'application/json')

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





if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
