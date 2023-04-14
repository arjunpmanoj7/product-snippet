/** @odoo-module alias=pos_kitchen_order.BookedOrderLine */

    import Registries from 'point_of_sale.Registries';
    import PosComponent from 'point_of_sale.PosComponent';

    export class KitchenScreenWidget extends PosComponent {
        setup() {
        super.setup();

    }
            get currentOrderKitchen() {
            const products = [];

            this.env.pos.get_order().get_orderlines().forEach(function(orderLine) {
                if(orderLine.get_product())
                    products.push(orderLine.get_product().display_name);
                    console.log('orderLine.get_product();', products)
            });
                    console.log('orderLwwwwwwwwwwwine.get_product();', products)
           return products;
        }
        async print_kitchenbill() {
             this.showScreen('ReceiptScreen');
        }
         get highlight() {
            return this.props.quotation !== this.props.selectedQuotation ? '' : 'highlight';
        }
        get currentOrder() {
         let product = this.env.pos.db.product_by_id[line.product_id[0]];
                let partner = this.env.pos.db.partner_by_id[this.props.quotation.partner_id[0]];
                console.log('product', product)
                console.log('partner', partner)
            return this.env.pos.get_order();
            }

    back() {
            this.showScreen('ProductScreen');
          }
    }
    KitchenScreenWidget.template = 'KitchenScreen';
    Registries.Component.add(KitchenScreenWidget)