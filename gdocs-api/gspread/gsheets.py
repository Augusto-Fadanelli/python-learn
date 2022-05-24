# Links úteis
# developers.google.com/sheets/api/quickstart/python
# docs.gspread.org/en/latest/
# console.cloud.google.com/apis/

# pip install gspread
# Necessário token

import gspread

if __name__ == '__main__':
    gc = gspread.service_account(filename='.service_account.json')
    sh = gc.open_by_key('1Ise8zJkIX91XAnEBVrduFuha2kWdYqjuVdbOnvQGAh8')

    worksheet = sh.worksheet('Página1')

    sheet = worksheet.get_all_records()
    print(sheet)

    '''
    while True:
        #search = input('Insira a célula a ser pesquisada: ')
        update = input('Insira a célula a ser substituída: ')
        print(update)
        worksheet.update(update, "teste")
        print(update)
    '''