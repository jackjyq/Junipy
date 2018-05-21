# API Documentation :memo:
---
This documentation covers the coffe shop order web API.

#### Media Type support
---
All server response bodies and request bodies MUST be valid **[JSON](https://tools.ietf.org/search/rfc4627)** messages.

### Orders :coffee:
---
The **Orders** URL (/orders/) is the base URL for reading and updating Order objects The table below shows all the Task-related operations, their URLs, methods, and payloads.

#### Table 1. Order operations
|    Operation  | URL | Method | Returns | Inputs |
| ---------- | --------------- |---- |--- |--- |
| CreateOrder | /orders |POST | PaymentURI, [order](#Order) | [order](#Order) |
| UpdateOrder | /orders/&lt;id&gt;/ | PUT | [order](#Order) | [order](#Order) |
| GetOrder| /orders/&lt;id&gt;| GET | [order](#Order) | none |
| CancelOrder| /orders/&lt;id&gt;| DELETE | [msg](#Msg) | none |
| ReleaseOrder | /orders/release/&lt;id&gt;| POST | [msg](#Msg) | none |
| PreparedOreder | /orders/prepare/&lt;id&gt;| PATCH | [order](#Order) | none |
| CheckOrderPaied| /orders/paied/&lt;id&gt;| GET | ture/false |none|
| GetAllOrders |  /orders | GET| [orderList](#OrderList)  | none |
| GetOpenOrders | /orders/open/ | GET | [orderList](#OrderList) | none |
| GetPaidOrders | /orders/paied/ | GET | [orderList](#OrderList) | none |
| GetUnPaidOrders | /orders/unpaied/ | GET | [orderList](#OrderList)  | none |
| GetReleaseOrders | /orders/release/ | GET | [orderList](#OrderList)  | none |

### Payment :dollar:

The **Payment** URL (/payments/) is the base URL for reading and updating User objects and supports the following operations:

#### Table 2. Payment operations
|    Operation    | URL | Method | Returns | Inputs |
| ---------- | --------------- |---- |--- |--- |
| CreatePayment | /payments/&lt;id&gt;/ |POST | [order](#Order) | [Payment](#Payment) |
| GetPayment | /payments/&lt;id&gt;| GET | [payment](#Payment) | none |

## Responses :eyes:
----
The Order API returns four possible payloads (as JSON object):
* [Order List](#OrderList)
* [Order](#Order)
* [Payment](#Payment)
* [Message](#MSG)

See below for details.

### <a name="OrderList"></a> Order List Json
A **order list** looks like this:
```json
[
  {
    "cost": 5.2,
    "coffeType": 1,
    "isPaied": false,
    "orderID": "201802180001",
    "isPrepared": false,
    "date": "2018-02-30T20:40:30",
    "addition": "no milk",
    "payment": {
    	"type": 2,
    	"amount": 5.2,
    	"cardNumber": "5037234512344321",
    	"cardName": "Josh Smith",
    	"expireDate": "03/20",
		"byBarista": false
    }
  },
  {
    "cost": 6.5,
    "coffeType": 5,
    "isPaied": false,
    "orderID": "201802180041",
    "isPrepared": true,
    "date": "2018-03-1T11:20:10",
    "addition": "",
    "payment": {
    	"type": 1,
    	"amount": 6.5,
    	"cardNumber": "",
    	"cardName": "",
    	"expireDate": "",
		"byBarista": true
    }
  }
]

```

See **[Data Elements](#Data)** for more information on each property.

---

#### <a name="Order"></a> Order Json
A **order** looks like this:
```json
{
    "cost": 5.2,
    "coffeType": 1,
    "isPaied": true,
    "orderID": "201802180001",
    "isPrepared": false,
    "date": "2018-02-30T20:40:30",
    "addition": "no milk",
    "payment": {
    	"type": 2,
    	"amount": 5.2,
    	"cardNumber": "5037234512344321",
    	"cardName": "Josh Smith",
    	"expireDate": "03/20"
    }
}
```
See **[Data Elements](#Data)** for more information on each property.

---

### <a name="Payment"></a> Payment Json
A **payment** looks like this:
```json
   {
    	"type": 1,
    	"amount": 5.2,
    	"cardNumber": "",
    	"cardName":"",
    	"expireDate": ""
    }
```

See **[Data Elements](#Data)** for more information on each property.

---

### <a name="Msg"></a> Error Msg
A **msg** example looks like this:
```json
   {
      "error": "Repeat order ID"
    }
```

See **[Data Elements](#Data)** for more information on each property.


## <a name="Request"> Request :icecream:
---
All payloads sent from the client to the server MUST be valid [JSON Media Type](https://tools.ietf.org/search/rfc4627) messages. The messages **SHOULD** be in simple name-value dictionary format based on the **INPUT** arguments from the [Order](#Order) Operations and the [Payment](#payment) Operations tables.

* [Order](#Order)
* [Payment](#Payment)

#### <a name="Create"> Create order
---
When the order was create, the *Payment* in Order Json must be **empty** and the *isPaid* should be **false** as well as *isPrepared*.
```json
{
    "cost": 5.2,
    "coffeType": 1,
    "isPaied": false,
    "orderID": "201802180001",
    "isPrepared": false,
    "date": "2018-02-30T20:40:30",
    "addition": "no milk",
    "payment": {
    	"type": 0,
    	"amount": 5.2,
    	"cardNumber": "",
    	"cardName": "",
    	"expireDate": ""
    }
}
```

#### <a name="Create"> Create payment
---
When the payment was create, the **type** should be **1** or **2**. If the type is 2, then *cardNumber* , *cardName* and *expireDate* are required parameters.

##### Cash payment
```json
  {
    	"type": 1,
    	"amount": 5.2,
    	"cardNumber": "",
    	"cardName": "",
    	"expireDate": ""
    }
```

##### Card payment
```json
    {
    	"type": 2,
    	"amount": 6.0,
    	"cardNumber": "5037234512344321",
    	"cardName": "Josh Smith",
    	"expireDate": "03/20"
    }
```

## <a name="Data"></a> Data Elements :sushi:
---
There is all the parameters describtion

##### <a name="OrderDetail"></a> Order detail

|    Name  | Meaning | Type | Optional
| --- | --- | --- |:----:|
| cost | Cost of coffee | Int | :heavy_multiplication_x: |
| [coffeeType](#CoffeeType) | The type of coffee | Int | :heavy_multiplication_x: |
| isPaied | The order is paied or not | Bool | :heavy_multiplication_x: |
| orderID | Order id | String | :heavy_multiplication_x:|
| isPrepared | Coffee is already to release | Bool | :heavy_multiplication_x:|
| date | Order create time | String | :heavy_multiplication_x:|
| addition | addition of Order | String | :heavy_check_mark:|
| payment| Payment detail | [Payment](#Payment) | :heavy_check_mark: |

##### <a name="PaymenrDetail"></a> Payment detail

|    Name  | Meaning | Type | Optional
| --- | --- | --- |:----:|
| [type](#PaymentType) | Type of payment | Int | :heavy_multiplication_x: |
| amount | The amount of bill | Int | :heavy_multiplication_x: |
| cardName | Name on credit card | String | :heavy_check_mark: |
| cardNumber | Credit card number | String |:heavy_check_mark: |
| expireDate | Credit expire date | String | :heavy_check_mark: |

#### <a name="CoffeeType"></a>  Coffe Type :coffee:
```python
	Espresso = 0
	Double_Espresso = 1
	Short_Macchiato = 2
	Long_Macchiato = 3
	Ristretto = 4
	Long_Black = 5
	Latte = 6
	Cappuccino = 7
	Flat_White = 8
	Piccolo_Latte = 9
	Mocha = 10
	Affogato = 11
```

#### <a name="PaymentType"></a> Payment Type :dollar:
```python
	Invailed = 0
	Cash = 1
	Card = 2
```


