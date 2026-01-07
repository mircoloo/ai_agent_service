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
    text: str

sample_invoice_text = """FATTURA N. 145/2024  DATA 12/02/2024

        Ragione Sociale: RISTORANTE IL GUSTO SRL
        Indirizzo: Via Roma 24 20121 Milano MI
        P.IVA: 09876543210  Codice Fiscale: 09876543210

        Cliente: FOOD SERVICE DISTRIBUTION SPA
        Via delle Industrie 45 20090 Assago MI
        P.IVA 12345678901

        Descrizione prodotti:
        fornitura materie prime gennaio 2024
        pomodori pelati scatola 12x 3.40
        pasta semola grano duro 20 kg 17.50
        olio extravergine oliva lattina 5l 28.90
        mozzarella fiordilatte 20kg 64.00

        Totale imponibile 113.80
        IVA 10% 11.38
        Totale fattura 125.18

        Modalità pagamento: Bonifico bancario 30 gg data fattura
        IBAN IT90 X054 2811 1010 0000 0123 456

        Note: consegna effettuata in data 05/02/2024
        Documento generato elettronicamente
        """