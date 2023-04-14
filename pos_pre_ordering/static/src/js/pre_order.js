odoo.define('pos_pre_ordering.PreOrder', function(require) {
'use strict';
   const { Gui } = require('point_of_sale.Gui');
   const PosComponent = require('point_of_sale.PosComponent');
   const { identifyError } = require('point_of_sale.utils');
   const ProductScreen = require('point_of_sale.ProductScreen');
   const { useListener } = require("@web/core/utils/hooks");
   const Registries = require('point_of_sale.Registries');
   const PaymentScreen = require('point_of_sale.PaymentScreen');
   class PreOrder extends PosComponent {
       setup() {
            super.setup();
            useListener('click', this.onClick);
        }

        onClick(ev) {
             this.showPopup('CreatePreOrderPopup',{
              title : this.env._t("Pre Order"),
              body : this.env._t("Sale Order Created!!!!!")
              });
            const context = {
                active_model: this.props.resModel,
            };
        }

    }
    PreOrder.template = 'PreOrder';
     ProductScreen.addControlButton({
        component: PreOrder,
        position: ['before', 'SetPricelistButton'],
        condition: function() {
            return this.env.pos.config.module_pos_restaurant && this.env.pos.unwatched.printers.length;
        },
    });

    Registries.Component.add(PreOrder);

    return PreOrder;
});