/** @odoo-module alias=pos_kitchen_order.book */
    import { Gui } from 'point_of_sale.Gui';
    import PosComponent from 'point_of_sale.PosComponent';
    import ProductScreen from 'point_of_sale.ProductScreen';
    import Registries from 'point_of_sale.Registries';
    import { useListener } from "@web/core/utils/hooks";
    import Chrome from "point_of_sale.Chrome";
    import { batched } from "point_of_sale.utils";
    var ReceiptScreen = require('point_of_sale.ReceiptScreen');
    var models = require('point_of_sale.models');
    import { debounce } from "@web/core/utils/timing";

    export class BookButton extends PosComponent {
     setup() {
           super.setup();
           useListener('click', this.onClick);
           this.quotations = this.env.pos.get_order().get_orderlines().length;
           console.log('aaaaaaaaaaaaaaa', this.quotations)

       }
        get currentOrderKitchen() {
           return this.env.pos.get_order();
        }

       async onClick() {
        let order = this.env.pos.get_order();
        const order_length = this.env.pos.get_order().get_orderlines().length;
        console.log('************', this.env.pos.get_order().get_orderlines())
        console.log('aaaaaaaaaaaaaaa', this.quotations)
        var quotations = this.quotations;
        this.showScreen('KitchenScreenWidget');

       }

    }
    BookButton.template = 'BookButton';;
    ProductScreen.addControlButton({
    component: BookButton,
    condition: function () {
        return true;
    },
    });

    Registries.Component.add(BookButton);
