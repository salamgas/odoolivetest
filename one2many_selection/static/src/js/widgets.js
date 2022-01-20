odoo.define('web_one2many_selectable_10.form_widgets', function (require) {
	"use strict";

	var core = require('web.core');
	var utils = require('web.utils');
	var _t = core._t;
	var QWeb = core.qweb;
	var fieldRegistry = require('web.field_registry');
	var ListRenderer = require('web.ListRenderer');
	var rpc = require('web.rpc');
	var FieldOne2Many = require('web.relational_fields').FieldOne2Many;

	ListRenderer.include({

		// Override this method to get delete button appear,disappear logic
		_updateSelection: function () {
	        this.selection = [];
	        var self = this;
	        var $inputs = this.$('tbody .o_list_record_selector input:visible:not(:disabled)');
	        var allChecked = $inputs.length > 0;
	        $inputs.each(function (index, input) {
	            if (input.checked) {
	                self.selection.push($(input).closest('tr').data('id'));
	            } else {
	                allChecked = false;
	            }
	        });
	        if(this.selection.length > 0){
	        	$('.button_delete_sale_order_lines').show()
	        	$('.button_replace_sale_order_lines').show()
	        }else{
	        	$('.button_delete_sale_order_lines').hide()
	        	$('.button_replace_sale_order_lines').hide()
	        }
	        this.$('thead .o_list_record_selector input').prop('checked', allChecked);
	        this.trigger_up('selection_changed', { selection: this.selection });
	        this._updateFooter();
	    },
	})


	var One2ManySelectable = FieldOne2Many.extend({
		template: 'One2ManySelectable',
		events: {
			"click .button_delete_sale_order_lines": "action_selected_lines",
			"click .button_replace_sale_order_lines": "action_replace_selected_lines",
		},
		start: function()
	    {
	    	this._super.apply(this, arguments);
			var self=this;		
	   },
		//passing ids to function
		action_selected_lines: function()
		{		
			var self=this;
			var selected_ids = self.get_selected_ids_one2many();

			if (selected_ids.length === 0)
			{
				this.do_warn(_t("You must choose at least one record."));
				return false;
			}
//			rpc.query({
//                'model': 'helpdesk.ticket',
//                'method': 'refund_product',
//                'args': [selected_ids, self.res_id],
            self.do_action({
                name: "Return Product",
                type: 'ir.actions.act_window',
                res_model: 'product.return.quantity',
                view_mode: 'form',
                view_type: 'form',
                views: [[false, 'form']],
                context: {'default_x_order_line': selected_ids, 'ticket': self.res_id},
                target: 'new',
            });
//            .then(function(result){
//                console.log(result, 'result')
//                if (result !== undefined) {
//                   self.do_action({
//                        name: "Return",
//                        type: 'ir.actions.act_window',
//                        res_model: 'stock.return.picking',
//                        view_mode: 'form',
//                        view_type: 'form',
//                        views: [[false, 'form']],
//                        context: result.context,
//                        target: 'new',
//                     });
//                }
//                else {
//                   self.trigger_up('reload');
//                }
//
//            });
		},

		action_replace_selected_lines: function()
		{
			var self=this;
			var selected_ids = self.get_selected_ids_one2many();

			if (selected_ids.length === 0)
			{
				this.do_warn(_t("You must choose at least one record."));
				return false;
			}
			console.log(selected_ids, 'selected_ids')
			self.do_action({
                name: "Replace Product With",
                type: 'ir.actions.act_window',
                res_model: 'product.product.replace',
                view_mode: 'form',
                view_type: 'form',
                views: [[false, 'form']],
                context: {'default_x_order_line': selected_ids, 'ticket': self.res_id},
                target: 'new',
             });
//			rpc.query({
//                'model': 'helpdesk.ticket',
//                'method': 'action_view_product_replace',
//                'args': [selected_ids],
//            });
		},
		_getRenderer: function () {
            if (this.view.arch.tag === 'kanban') {
                return One2ManyKanbanRenderer;
            }
            if (this.view.arch.tag === 'tree') {
                return ListRenderer.extend({
                    init: function (parent, state, params) {
                        this._super.apply(this, arguments);
                        this.hasSelectors = true;
                    },
                });
            }
            return this._super.apply(this, arguments);
        },
		//collecting the selected IDS from one2manay list
		get_selected_ids_one2many: function () {
            var self=this;
            var ids =[];
            this.$el.find('td.o_list_record_selector input:checked')
                    .closest('tr').each(function () {
                        ids.push(parseInt(self._getResId($(this).data('id'))));
            });
            return ids;
        },

        _getResId: function (recordId) {
            var record;
            utils.traverse_records(this.recordData[this.name], function (r) {
                if (r.id === recordId) {
                    record = r;
                }
            });
            return record.res_id;
        },
	});

	// register unique widget, because Odoo does not know anything about it
	//you can use <field name="One2many_ids" widget="x2many_selectable"> for call this widget
	fieldRegistry.add('one2many_selectable', One2ManySelectable);
});