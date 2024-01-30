from datetime import date, datetime


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')  # Dia, Mês e Ano com 4 dígitos


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formate_float_str_moeda(valor: float) -> str:
    """Na programação precisamos usar o '.' como separador de campos decimais
    entretando a moeda brasileira Real usa a vírgula como esse separador, por isso
    essa função realiza essa formatação."""
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
