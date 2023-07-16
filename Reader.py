import qrcode
import os
UInp = ''


def create():
    global UInp
    data = str(input('Enter the desired data to put on a QR code'))

    QR = qrcode.make(data)
    QR.save('C:/Users/Adam/Documents/MyQR.png')
    print('QR code created successfully')
    UInp = input('do you want to delete the file?')
    if UInp == 'yes':
        os.remove('C:/Users/Adam/Documents/MyQR.png')
        print('The QR code file has been deleted successfully')
        UInp = input('Do you want to create another QR code?')
        if UInp == 'yes':
            create()
        else:
            quit()

    else:
        UInp = input('Do you want to create another QR code?\nbut note that the previous QR code will be deleted')
        if UInp == 'yes':
            create()
        else:
            quit()


create()
