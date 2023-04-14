from odoo import models, fields
import requests
import json


class ZatacIntegration(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        url = "https://kixq9sqvjc.execute-api.ap-south-1.amazonaws.com/test/api/v1/proto/csrRequest"

        payload = json.dumps({
            "csrInputs": {
                "otp": "123345",
                "commonName": "TST-886431145-300055184400003",
                "serialNumber": "1-TST|2-TST|3-ed22f1d8-e6a2-1118-9b58-d9a8f11e44yt",
                "organizationIdentifier": "300055184400003",
                "organizationUnitName": "Riyadh",
                "organizationName": "Antna Technologies",
                "countryName": "SA",
                "invoiceType": "1100",
                "location": "Riyadh",
                "industry": "Civil"
            }
        })
        headers = {
            'Authorization': 'eyJraWQiOiJYbUU2MnZzZkdkZWI0bzEyUWlcL0F5OEcrcUQxand2N0JwRGN6aWdrM2ZVaz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMDBiNWE5Yi0wNzBkLTQzODYtYWJiZi1kNjZlNmE4OWFkMDQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX0pBUHpIMk9hRSIsInZlcnNpb24iOjIsImNsaWVudF9pZCI6IjZxNWoydmo5YjB1cXAzZWtrdXJvc2gxOWVmIiwiZXZlbnRfaWQiOiIxOWM4ZDU0NS0yODZhLTQ3NzktYTNhZC1hY2Q0NzY1ZDQyNTUiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIGh0dHBzOlwvXC9hcC1zb3V0aC0xLmNvbnNvbGUuYXdzLmFtYXpvbi5jb21cL2FwaSIsImF1dGhfdGltZSI6MTY3MzUxMjU1MiwiZXhwIjoxNjczNTk4OTUyLCJpYXQiOjE2NzM1MTI1NTIsImp0aSI6IjQwNWJiOGU4LWFiMTUtNDUwOC1hYTcxLTEwNzRhMGMzMWRjMCIsInVzZXJuYW1lIjoiYjAwYjVhOWItMDcwZC00Mzg2LWFiYmYtZDY2ZTZhODlhZDA0In0.IGCLM5j8CvhVTCak9hPfEYc5IJv0hETm22fAcnl9McvGcUn_BoWRtw5GbGlVhl8GhzTUay99geUgGUDdSyaRyuj6Z8WgbozTSR7BZeAFhjUMyGra5KiynQsKGrJG8hjr3iq7NluKItyfkLacxZY4cmO8rhCvtPZq_KJ8qjkYR064ypcrQZPG6P6IB0it_iMR5NBEqWbQO3gbcfE38Trsl5uMtu6zsf5ryYVR4OgJjFgdIq2qK2P4v8_hzJ2XUVWcLT6Q8UrUEdAsMKJGrP9fKxrL0K5s5WC2nHk2mKAoVO-w-895IC7uqF46RcbAEc9GsfpnKcdr0nwzhzUMeZk7hw',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

        return super(ZatacIntegration, self).action_confirm()


class InheritResCompany(models.Model):
    _inherit = 'res.company'

    common_name = fields.Char(
        string='Common Name'
    )
    egs_serial_number = fields.Char(
        string='EGS Serial Number'
    )
    orgnization_identifier = fields.Char(string='Organization Identifier')
    organization_unit_name = fields.Char(string='Organization Unit Name')
    api_link = fields.Char(string='Api Link')
    country_name = fields.Char(string='Country Name')
    invoice_type = fields.Char(string='Invoice Type')
    industry = fields.Char(string='Industry')
    otp = fields.Char(string='OTP')
    certificate = fields.Char(string='Certificate')
    zatca_status = fields.Char(string='Zatca Status')
    testing = fields.Char(string='Testing')
    private_key = fields.Char(string='Private Key')

