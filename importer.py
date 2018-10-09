import csv

input_format = [
    'Handle',
    'Title',
    'Body (HTML)',
    'Vendor',
    'Type',
    'Tags',
    'Published',
    'Option1 Name',
    'Option1 Value',
    'Option2 Name',
    'Option2 Value',
    'Option3 Name',
    'Option3 Value',
    'Variant SKU',
    'Variant Grams',
    'Variant Inventory Tracker',
    'Variant Inventory Qty',
    'Variant Inventory Policy',
    'Variant Fulfillment Service',
    'Variant Price',
    'Variant Compare At Price',
    'Variant Requires Shipping',
    'Variant Taxable',
    'Variant Barcode',
    'Image Src',
    'Image Position',
    'Image Alt Text',
    'Gift Card',
    'SEO Title',
    'SEO Description',
    'Google Shopping / Google Product Category',
    'Google Shopping / Gender',
    'Google Shopping / Age Group',
    'Google Shopping / MPN',
    'Google Shopping / AdWords Grouping',
    'Google Shopping / AdWords Labels',
    'Google Shopping / Condition',
    'Google Shopping / Custom Product',
    'Google Shopping / Custom Label 0',
    'Google Shopping / Custom Label 1',
    'Google Shopping / Custom Label 2',
    'Google Shopping / Custom Label 3',
    'Google Shopping / Custom Label 4',
    'Variant Image',
    'Variant Weight Unit',
    'Variant Tax Code'
]

output_format = [
    'unique_id*',
    'name*',
    'price*',
    'price_after_discount',
    'category*',
    'sub_category',
    'photos*',
    'description*',
    'tags*',
    'shipping_regular_post',
    'shipping_regular_post_additional_product',
    'shipping_courier',
    'shipping_courier_additional_product',
    'shipping_abroad',
    'shipping_abroad_additional_product',
    'shipping_pickup',
    'department',
    'inventory',
    'active'
]

SHOPIFY_EXPORT_FILE = 'shopify_products_export.csv'
export_rows = []

with open(SHOPIFY_EXPORT_FILE, encoding='utf8') as importCsv:
    reader = csv.DictReader(importCsv, fieldnames=input_format)
    index = 0
    for idx, row in enumerate(reader, start=0):
        html = row['Body (HTML)']
        if (html):
            html = html.replace('\n', '')
            try:
                price = int(float(row['Variant Price'])) + 10
                pass
            except ValueError:
                price = row['Variant Price']
                print('Price is not a number: ' + row['Variant Price'])
            export_row = {
                'unique_id*': index,
                'name*': row['Title'],
                'price*': price,
                # FIXME: parse it and update it
                'price_after_discount': row['Variant Compare At Price'],
                'category*': "אמנות ,Do It Yourself",
                'sub_category': 'ציור',
                'photos*': row['Image Src'],
                # FIXME: add array of photos
                'description*': html,
                # 'tags*': row['Tags'].replace('\n', ''),
                'tags*': 'צביע לפי מספרים, דיוקן אישי',
                'shipping_regular_post': '',
                'shipping_regular_post_additional_product': '',
                'shipping_courier': '',
                'shipping_courier_additional_product': '',
                'shipping_abroad': '',
                'shipping_abroad_additional_product': '',
                'shipping_pickup': 'תל אביב והמרכז',
                'department': '',
                'inventory': 1,
                'active': 'פעיל'
            }
            export_rows.append(export_row)
            index += 1

with open('output.csv', 'w', encoding='utf8') as exportCsv:
    writer = csv.DictWriter(exportCsv, fieldnames=output_format)
    writer.writeheader()
    for row in export_rows:
        writer.writerow(row)
