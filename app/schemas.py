from pydantic import BaseModel, Field

class InvoiceCategoryOutput(BaseModel):
    invoice_number: str = Field(..., description="Numero della fattura.")
    invoice_date: str = Field(..., description="Data della fattura.")
    supplier_name: str = Field(..., description="Nome del fornitore.")
    total_amount: float = Field(..., description="Importo totale della fattura.")
    items: list['Item'] = Field(..., description="Elenco degli articoli nella fattura la quantità e il prezzo associato.")
    
    
class Item(BaseModel):
    description: str = Field(..., description="Descrizione dell'articolo.")
    quantity: int = Field(..., description="Quantità dell'articolo.")
    price: float = Field(..., description="Prezzo unitario dell'articolo.")
    
class ChatRequest(BaseModel):
    req_text: str =  Field(None, description="The chat request text")
    
class ChatResponse(BaseModel):
    res_text: str