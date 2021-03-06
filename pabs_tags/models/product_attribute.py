from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError, RedirectWarning
from odoo.osv import expression


class ProductTemplateAttributeLine(models.Model):
    """Attributes available on product.template with their selected values in a m2m.
    Used as a configuration model to generate the appropriate product.template.attribute.value"""

    _inherit = 'product.template.attribute.line'
    x_is_print = fields.Boolean(string="Print In Price Tags", default=False)
    x_print_variant_upper = fields.Boolean(string="Print Upper", default=False)

    @api.onchange('value_ids')
    def x_category_id_filter(self):
        res = {}
        ls = []

        print(self.product_tmpl_id.categ_id.complete_name.replace(" ", "").strip())
        category = self.env['product.category'].search([('name', 'in', self.product_tmpl_id.categ_id.complete_name.replace(" ", "").split("/"))])
        print(category)
        res['domain'] = {'attribute_id': [('x_category_id', 'in', category.ids)]}
        return res


    # @api.onchange('value_ids')
    # def make_printable(self):
        # print(self.mapped('value_ids'))
        # action = self.env.ref('base.action_res_users')
        # msg = _("You cannot create a new user from here.\n To create new user please go to configuration panel.")
        # raise RedirectWarning(msg, action.id, _('Go'))
        # return {'warning': {'title': 'Warning', 'message': 'Do You want the added attribute to be printable ?'},'value': {'x_is_print': True}}



    # def test(self):
    #     return {
    #         'name': 'make printable?',
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'product.make.printable',
    #         'view_id': self.env.ref('pabs_tags.make_printable').id,
    #         'view_mode': 'form',
    #         'target': 'new',
    #     }

    # def write(self, values):
    #     res = super(ProductTemplateAttributeLine, self).write(values)
    #     return [res, self.test()]

    # def action_view_invoice(self):
        # invoices = self.mapped('invoice_ids')
        # action = self.env.ref('pabs_tags.action_make_printable').read()[0]
        # form_view = [(self.env.ref('account.view_move_form').id, 'form')]
        # if 'views' in action:
        #     action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
        # else:
        #     action['views'] = form_view
        # action['res_id'] = invoices.id
        # else:
        #     action = {'type': 'ir.actions.act_window_close'}
        #
        # context = {
        #     'default_type': 'out_invoice',
        # }
        # if len(self) == 1:
        #     context.update({
        #         'default_partner_id': self.partner_id.id,
        #         'default_partner_shipping_id': self.partner_shipping_id.id,
        #         'default_invoice_payment_term_id': self.payment_term_id.id or self.partner_id.property_payment_term_id.id or self.env['account.move'].default_get(['invoice_payment_term_id']).get('invoice_payment_term_id'),
        #         'default_invoice_origin': self.mapped('name'),
        #         'default_user_id': self.user_id.id,
        #     })
        # action['context'] = context
        # return action



class ProductTemplateAttributeValue(models.Model):
    """Materialized relationship between attribute values
    and product template generated by the product.template.attribute.line"""

    _inherit = 'product.template.attribute.value'
    x_is_print = fields.Boolean(string="Print In Price Tags", related="attribute_line_id.x_is_print")
    x_print_variant_upper = fields.Boolean(string="Print Upper", related="attribute_line_id.x_print_variant_upper")


# class ProductTemplate(models.Model):
#     _inherit = 'product.template'
#
#     @api.onchange('attribute_line_ids')
#     def make_printable(self):
#         print('123')

# class Product(models.Model):
#     _inherit = 'product.template'
#
#     def test(self):
#         return {
#             'name': 'make printable?',
#             'type': 'ir.actions.act_window',
#             'res_model': 'product.make.printable',
#             'view_id': self.env.ref('pabs_tags.make_printable').id,
#             'view_mode': 'form',
#             'target': 'new',
#         }


class ProductAttribute(models.Model):
    _inherit = 'product.attribute'
    x_category_id = fields.Many2many('product.category', string='Product Category')



