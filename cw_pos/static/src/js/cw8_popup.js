odoo.define('point_of_sale.CreateSaleOrderPopup', function(require){
    'use strict';
///** @odoo-module */
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");
    const { _lt } = require('@web/core/l10n/translation');
    var rpc =require('web.rpc')
    const ajax = require('web.ajax');
    const { useState, onMounted } = owl;
    var this_orderline;
    class CreateSaleOrderPopup extends AbstractAwaitablePopup {
//    template:'CreateSaleOrderPopup',
        setup() {
            super.setup();
            console.log('this',this)
             useListener('add_to_line', this._onClickReOrderConfirm);
        }

        cw_uom_select(e) {
                var quantity=this.env.pos.selectedOrder.selected_orderline.quantity
                var unit=this.env.pos.selectedOrder.selected_orderline.product.uom_id[0]
                var product_id=this.env.pos.selectedOrder.selected_orderline.product.id
                var option = $('#select').val();
                ajax.jsonRpc('/pos_request_route', 'call',{
                            product_id : product_id,
                             option: option,
                             quantity:quantity,
                             unit:unit

                        }).then(function(result){
                            console.log('res', result)
                             $('#value').text(result['calculation'])
                        })

            }
        _onClickReOrderConfirm()
        {
                var cw = $('#value')[0].innerText
                var product_id =  this.env.pos.selectedOrder.selected_orderline.product.id
                var product = this.env.pos.db.get_product_by_id(product_id);
                var quantity = '';
                $('.orderline.selected')[0].children[2].innerText = 'Quantiy: ' + cw
                var self = this.env.pos.selectedOrder.selected_orderline.product.pos.session_orders
                this.env.posbus.trigger('close-popup', {
                popupId: this.props.id
                });

        }


    }
    CreateSaleOrderPopup.template = 'CreateSaleOrderPopup';

//
    CreateSaleOrderPopup.defaultProps = {
        confirmText: _lt('Confirm'),
        cancelText: _lt('Cancel'),
        title: _lt('Confirm ?'),
        body: '',
    };

    Registries.Component.add(CreateSaleOrderPopup);

    return CreateSaleOrderPopup;
});
