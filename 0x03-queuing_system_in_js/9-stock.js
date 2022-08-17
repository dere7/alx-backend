import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

function getItemById(id) {
  const products = listProducts.filter(product => product.itemId === id);
  if (products.length === 0) return null;
  else return products[0];
}

const app = express();
const client = redis.createClient();

app.get('/list_products', (req, res) => {
  res.send(listProducts);
  res.end();
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  getCurrentReservedStockById(itemId).then(item => {
    if (item) {
      res.send(item);
    } else {
      res.send({ status: 'Product not found' });
    }
    res.end();
  });
});
app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (item) {
    if (item.initialAvailableQuantity > 0) {
      reserveStockById(itemId, 1);
      res.send({ status: 'Reservation confirmed', itemId });
    } else {
      res.send({ status: 'Not enough stock available', itemId });
    }
  } else {
    res.send({ status: 'Product not found' });
  }
  res.end();
});

async function reserveStockById(itemId, stock) {
  const setAsync = promisify(client.set).bind(client);
  await setAsync(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  try {
    const getAsync = promisify(client.get).bind(client);
    const reserved = await getAsync(itemId);
    const item = getItemById(itemId);
    if (!item) return null;
    item.currentQuantity = item.initialAvailableQuantity - reserved;
    return item;
  } catch (e) {
    console.error(e);
  }
}

app.listen(1245);
