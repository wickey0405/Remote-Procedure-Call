class Display{
    #message = "";
    constructor(){}

    disp(){
        console.log(this.#message)
    }

    setMessage(newMessage){
        this.#message = newMessage;
    }
}

module.exports = Display;