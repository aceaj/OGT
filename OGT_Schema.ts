

// Create a schema for classes to easily interact from python

const OV: string="Hello";


class PlantBay{
    private name:string;
    constructor(name:string){
        this.name = name;
    }
    public getName():string{
        return this.name
    }
}

const Bay1Test=new PlantBay("A1")