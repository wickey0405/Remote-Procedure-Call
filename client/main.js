const fs = require('fs')
const fetchData = require("./myFetch")
const Display = require('./display')

display = new Display();

// 接続先アドレス定義
const serverAddress = 'http://localhost:3000'
// JSONファイルの読み込み
const jsonData = JSON.parse(fs.readFileSync("./inputJSON/inputDataSort.json", "utf-8"));

// JSONデータをPOST＆サーバからのレスポンス表示
fetchData(jsonData, serverAddress, display)

// 一気にテストする場合は以下を使用する
const testJSONList = [
    "./inputJSON/inputDataFloor.json",
    "./inputJSON/inputDataNroot.json",
    "./inputJSON/inputDataReverse.json",
    "./inputJSON/inputDataValidAnagram.json",
    "./inputJSON/inputDataSort.json"
]
testJSONList.map(file=>JSON.parse(fs.readFileSync(file, "utf-8")))
    .forEach(jsonData=>fetchData(jsonData, serverAddress, display))