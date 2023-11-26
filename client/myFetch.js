const fetchData = async (body, serverAddress, display) => {
    try{
        const response = await fetch(serverAddress,{
            method: "POST",
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body),
        })
        if (!response.ok){
            throw new Error(`HTTP Error: ${response.status}`)
        }
        const data = await response.json()
        display.setMessage(data)
        console.log(data)
    } catch(err){
        console.error(err)
    }
}

module.exports = fetchData