odoo.define('pos_delete_orderline.DeleteOrderLines', function(require) {
'use strict';
    const { useState, useRef, onPatched } = owl;
    const { useListener } = require("@web/core/utils/hooks");
    const { onChangeOrder } = require('point_of_sale.custom_hooks');
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const Orderline = require('point_of_sale.Orderline');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const OrderWidget = require('point_of_sale.OrderWidget');
    const { Gui } = require('point_of_sale.Gui');




    const OrderLineDelete = (Orderline) =>
       class extends Orderline {

       async onClickUploadProduct(ev) {
//       window.location.reload();
        var values = this.env.pos.selectedOrder.selected_orderline.product.pos.session_orders
        console.log('hiiefeidsdsd',values)
        values.forEach(element => {
        console.log(element['product_temp_con'])
 

        });

       this.showPopup('CreateSaleOrderPopup',{
              title : this.env._t("Add CW Quantity"),
              body : this.env._t("Sale Order Created!!!!!")
              });
            const context = {
                active_model: this.props.resModel,
            };

        }

        };
    Registries.Component.extend(Orderline, OrderLineDelete);
    return OrderWidget;

});
