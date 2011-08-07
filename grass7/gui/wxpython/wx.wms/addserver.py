#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Thu Jul 14 06:22:35 2011

import wx
import os
import uuid
from wx.lib.pubsub import Publisher
from BeautifulSoup import BeautifulSoup, Tag, NavigableString, BeautifulStoneSoup
from ServerInfoAPIs import addServerInfo, removeServerInfo, updateServerInfo, initServerInfoBase, getAllRows
from LoadConfig import loadConfigFile
from savepopup import SavePopUp


# begin wxGlade: extracode
# end wxGlade

class ServerData():
    pass


class ServerAdd(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ServerAdd.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.StatusBar = self.CreateStatusBar(1, 0)
        self.Servers = wx.StaticText(self, -1, "  Servers")
        self.ServerList = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.static_line_1 = wx.StaticLine(self, -1)
        self.ServerName = wx.StaticText(self, -1, "  ServerName*")
        self.ServerNameText = wx.TextCtrl(self, -1, "")
        self.URL = wx.StaticText(self, -1, "  URL*")
        self.URLText = wx.TextCtrl(self, -1, "")
        self.Username = wx.StaticText(self, -1, "  Username*")
        self.UsernameText = wx.TextCtrl(self, -1, "")
        self.Password = wx.StaticText(self, -1, "  Password")
        self.PasswordText = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.PasswordExplain = wx.StaticText(self, -1, "  Note: Password will be stored as a plain text")
        self.static_line_2 = wx.StaticLine(self, -1)
        self.Save = wx.Button(self, -1, "Save")
        self.Remove = wx.Button(self, -1, "Remove")
        self.AddNew = wx.Button(self, -1, "AddNew")
        self.Quit = wx.Button(self, -1, "Quit")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnServerList, self.ServerList)
        self.Bind(wx.EVT_TEXT, self.OnText, self.ServerNameText)
        self.Bind(wx.EVT_TEXT, self.OnText, self.URLText)
        self.Bind(wx.EVT_TEXT, self.OnText, self.UsernameText)
        self.Bind(wx.EVT_TEXT, self.OnText, self.PasswordText)
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.Save)
        self.Bind(wx.EVT_BUTTON, self.OnRemove, self.Remove)
        self.Bind(wx.EVT_BUTTON, self.OnAddNew, self.AddNew)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.Quit)
        # end wxGlade
        
        
        #sudeep code starts
        if( not loadConfigFile(self)):
            print 'Config File Error, Unable to start application...'
            self.Close()
        
        self.soup, open = initServerInfoBase('ServersList.xml')
        if(not open):
            return
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.__populate_URL_List(self.ServerList)
        Publisher().subscribe(self.OnWMSMenuClose, ("WMS_Menu_Close"))
        Publisher().subscribe(self.OnPopupSaveRequest, ("PopupSaveRequest"))
        Publisher().subscribe(self.OnPopupNotSaveRequest, ("PopupNotSaveRequest"))
        Publisher().subscribe(self.OnPopupCancelRequest, ("PopupCancelRequest"))
        self.editOn = False
        self.selectedUid = None
        #sudeep code ends

    def __set_properties(self):
        # begin wxGlade: ServerAdd.__set_properties
        self.SetTitle("AddServer")
        self.SetSize((422, 250))
        self.StatusBar.SetStatusWidths([-1])
        # statusbar fields
        StatusBar_fields = ["StatusBar"]
        for i in range(len(StatusBar_fields)):
            self.StatusBar.SetStatusText(StatusBar_fields[i], i)
        self.Servers.SetMinSize((90, 17))
        self.ServerList.SetMinSize((189, 29))
        self.ServerName.SetMinSize((96, 20))
        self.ServerNameText.SetMinSize((189, 25))
        self.URL.SetMinSize((90, 20))
        self.URLText.SetMinSize((189, 25))
        self.Username.SetMinSize((90, 20))
        self.UsernameText.SetMinSize((189, 25))
        self.Password.SetMinSize((90, 20))
        self.PasswordText.SetMinSize((189, 25))
        self.PasswordExplain.SetMinSize((303, 20))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ServerAdd.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.Servers, 0, 0, 0)
        sizer_2.Add(self.ServerList, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_3.Add(self.ServerName, 0, 0, 0)
        sizer_3.Add(self.ServerNameText, 0, 0, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add(self.URL, 0, 0, 0)
        sizer_4.Add(self.URLText, 0, 0, 0)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.Username, 0, 0, 0)
        sizer_5.Add(self.UsernameText, 0, 0, 0)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.Password, 0, 0, 0)
        sizer_6.Add(self.PasswordText, 0, 0, 0)
        sizer_1.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_1.Add(self.PasswordExplain, 0, 0, 0)
        sizer_1.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_7.Add(self.Save, 0, 0, 0)
        sizer_7.Add(self.Remove, 0, 0, 0)
        sizer_7.Add(self.AddNew, 0, 0, 0)
        sizer_7.Add(self.Quit, 0, 0, 6)
        sizer_1.Add(sizer_7, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade
    def valueExists(self,dict, newServerName):
        print 'Enter here'
        print newServerName
        try:
            for key, value in dict.items():
                #print key, value.servername
                if(value.servername == newServerName):
                    print 'returning true'
                    return True
            print 'returning False'
            return False
        except:
            print 'Exception while iterating dictionary elements'
            return False
    def OnSave(self, event): # wxGlade: ServerAdd.<event_handler>
        #print "Event handler `OnSave' not implemented"
        print '-------------------------------------------------------------------> OnSave'
        newServerName = unicode(self.ServerNameText.GetValue())
        newUrl = self.URLText.GetValue()
        newUserName = self.UsernameText.GetValue()
        newPassword = self.PasswordText.GetValue()
        
        if(not self.allFieldsValid(newServerName, newUrl, newUserName, newPassword)):
            return
        
        
        if(not newUrl.startswith('http://')):
            newUrl = 'http://'+newUrl
        
        
        print newServerName
        print 'check12'
        
        if(self.selectedUid == None):
            update = False
        else:
            update = True
        '''print newServerName
        print self.map_servernameTouid
        if(self.map_servernameTouid.has_key(newServerName)):
            CurrentUid = self.map_servernameTouid[newServerName]
            update = True
            print 'key present'
        else:
            print 'key not present'
            CurrentUid = None
            update = False
        if(self.servers.has_key(Uid)):
            update = True
            #print 'Server Name already exists'
            #return
        else:
            update = False'''
            
       
        
        serverData = ServerData()
        #self.ServerList.Append(newServerName+" "+newUrl)
        
        url = newUrl.split()
        #if(len(newUrl) != 0 and len(newServerName) != 0 and len(newUserName) !=0 and len(newPassword) != 0 ):
        if(len(newUrl) != 0 and len(newServerName) != 0):
            if(not self.selectedServer.servername == newServerName):
                if(self.valueExists(self.servers, newServerName)):
                    print 'Please Enter a different Servername'
                    return
            #del self.servers[self.selectedUid]
            serverData.servername = newServerName
            serverData.url = newUrl
            serverData.username = newUserName
            serverData.password = newPassword
            
            
            if(update):
                if(updateServerInfo(self.soup, self.soup.serverinfo, self.selectedUid, newServerName, newUrl, newUserName, newPassword)):
                    print 'update save successful'
                    self.servers[self.selectedUid] = serverData
                    del self.map_servernameTouid[self.selectedServer.servername]
                    self.selectedServer = serverData
                    self.map_servernameTouid[newServerName] = self.selectedUid
                    self.saveXMLData()
                    msg = self.servers
                    Publisher().sendMessage(("update.serverList"), msg)
                else:
                    print 'update save not successful'
            else:    
                uid = str(uuid.uuid4())
                
                if(addServerInfo(self.soup, self.soup.serverinfo, uid, newServerName, newUrl, newUserName, newPassword)):
                    print 'soup save successfully'
                    self.selectedUid = uid
                    self.servers[self.selectedUid] = serverData
                    self.selectedServer = serverData
                    self.map_servernameTouid[newServerName] = uid
                    self.saveXMLData()
                    msg = self.servers
                    Publisher().sendMessage(("update.serverList"), msg)
                else:
                    print "False returned by addServerInfo, save not successful"
            '''
            f = open('serverList.txt','a')
            f.write(newServerName+" "+newUrl+ " "+newUserName+" "+newPassword+"\n")
            f.close()
            '''
            self.selectedURL = newUrl
            print self.selectedURL
            #print self.servers
            self.__update_URL_List()
  	    #Update_Url_List(newServerName+" "+newUrl)
        else:
            print "Please Fill servername and url fields"
        self.editOn = False
        if(event):
            event.Skip()

    def OnRemove(self, event): # wxGlade: ServerAdd.<event_handler>
        print '-------------------------------------------------------------------> OnRemove'
        if(self.selectedUid == None):
            print 'No Uid is selected....Remove Unsuccessful'
            return
        else:
            if(removeServerInfo(self.soup, self.selectedUid)):
                print 'remove successful'
                del self.map_servernameTouid[self.selectedServer.servername]
            else:
                print 'remove unsuccessful'
                return
            #print self.servers
            
            del self.servers[self.selectedUid]
            self.selectedUid = None
            self.__update_URL_List()
            
            self.ServerNameText.Clear()
            self.PasswordText.Clear()
            self.URLText.Clear()
            self.UsernameText.Clear()
            #print self.servers
            self.saveXMLData()
            msg = self.servers
            Publisher().sendMessage(("update.serverList"), msg)
        
        #print "Event handler `OnRemove' not implemented"
        self.editOn = False
        event.Skip()

    def OnAddNew(self, event): # wxGlade: ServerAdd.<event_handler>
        print '-------------------------------------------------------------------> OnAddNew'
        #print "Event handler `OnAddNew' not implemented"
        self.selectedUid = None
        self.ServerNameText.Clear()
        self.PasswordText.Clear()
        self.URLText.Clear()
        self.UsernameText.Clear()
        self.editOn = False
        event.Skip()
    
    def OnQuit(self, event): # wxGlade: ServerAdd.<event_handler>
        print '-------------------------------------------------------------------> OnQuit'
        print 'onQuit pressed'
        if(self.editOn):
            print "Do you want to save the unsaved changes ?"
            SavePopUp()
        self.saveXMLData()
        msg = self.servers
        Publisher().sendMessage(("Add_Server_Frame_Closed"), msg)
        self.Destroy()
        #exit()
        #self.Close()
        '''out = open('serverList.txt','w')
        for k,v in self.servers.iteritems():
            out.write(v.servername+" "+v.url+" "+v.username+" "+v.password+"\n")
        exit()'''
        #ServerAdd.Close()
        #print "Event handler `OnQuit' not implemented"
        event.Skip()

    def OnServerList(self, event): # wxGlade: ServerAdd.<event_handler>
        print '-------------------------------------------------------------------> OnServerList'
        #print self.ServerList.CurrentSelection
        url = self.ServerList.GetValue()
        print 'here'
        print url
        urlarr = url.split(self.name_url_delimiter)
        print urlarr
        #print self.servers
        if(len(urlarr)==2):
            uid = self.map_servernameTouid[urlarr[0]]
            self.selectedUid = uid
            self.selectedServer = self.servers[uid]
            print self.selectedServer
            self.ServerNameText.SetValue(self.selectedServer.servername)
            self.URLText.SetValue(self.selectedServer.url)
            self.UsernameText.SetValue(self.selectedServer.username)
            self.PasswordText.SetValue(self.selectedServer.password)
        else:
            print "Wrong format of URL selected"
            
        #self.ServerNameText.SetValue(self.servers)
        event.Skip()

    def OnText(self, event): # wxGlade: ServerAdd.<event_handler>
        self.editOn = True
        event.Skip()
    #wxGlade methods ends
    
    #Sudeeps methods start
    def __populate_URL_List(self, ComboBox):
        self.servers, self.map_servernameTouid = getAllRows(self.soup)
        for key, value in self.servers.items():
            ComboBox.Append(value.servername+self.name_url_delimiter+value.url)
            #ComboBox.Append(value.servername+" "+value.url)
        #print self.servers
        return
    
    def __update_URL_List(self):
        self.ServerList.Clear()
        for key,value in self.servers.iteritems():
            #name = v.servername+" "+v.url
            self.ServerList.Append(value.servername+self.name_url_delimiter+value.url)
            #self.ServerList.Append(name)

    def saveXMLData(self):
        xml = self.soup.prettify()
        try:
            f = open('templist.xml','w')
            f.write(xml)
            f.close()
        except:
            print 'Unable to write in templist.xml file, Save not successful'
            return False
        try:    
            os.system('chmod 777 ServersList.xml')
            os.system("cp templist.xml ServersList.xml")
            #f = open('ServersList.xml','w')
        except:
            #print 'cant open file in write mode'
            print 'cp templist.xml ServersList.xml failed'
            print 'Save not successful'
            return False
        return True
    
    def allFieldsValid(self, newServerName, newUrl, newUserName, newPassword):
        if(newServerName.count(self.name_url_delimiter)>0):
                print "Warning: UserName cannot consist of "+self.name_url_delimiter
                print "Please give another username, save failed..."
                return False
            
        if(newUrl.count(self.name_url_delimiter)>0):
                print "Warning: URL cannot consist of "+self.name_url_delimiter
                print "Change in config file required to use different character as delimeter which doesnot appears in url"
                return False
            
        character = '>'
        if(newServerName.count(character) > 0 or newUrl.count(character) > 0 or newUserName.count(character) > 0 or newPassword.count(character) > 0):
            print character+' is not allowed in a Field'
            return False

        character = '<'
        if(newServerName.count(character) > 0 or newUrl.count(character) > 0 or newUserName.count(character) > 0 or newPassword.count(character) > 0):
            print character+' is not allowed in a Field'
            return False
        
        character = '&'
        if(newServerName.count(character) > 0 or newUrl.count(character) > 0 or newUserName.count(character) > 0 or newPassword.count(character) > 0):
            print character+' is not allowed in a Field'
            return False
        
        return True
    


    def OnWMSMenuClose(self, msg):
        self.Close()
        self.Destroy()
        return
    
    def OnPopupSaveRequest(self, msg):
        self.OnSave(None)
        self.saveXMLData()
        msg = self.servers
        Publisher().sendMessage(("Add_Server_Frame_Closed"), msg)
        self.Quit
        self.Close()
        #self.Destroy()
    
    def OnPopupNotSaveRequest(self, msg):
        self.saveXMLData()
        msg = self.servers
        Publisher().sendMessage(("Add_Server_Frame_Closed"), msg)
        self.Close()
        self.Destroy()

    def OnPopupCancelRequest(self, msg):
        return
# end of class ServerAdd

def AddServerFrame(parentWMS):
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = ServerAdd(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = ServerAdd(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
