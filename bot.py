import discord
import datetime


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    bar = discord.Game("데이터 수집 중...")
    await client.change_presence(status=discord.Status.online, activity=bar)


spe = ['?', '/', ';', ':', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
       '(', ')', '-', '_', '=', '+', ',', '.', '<', '>', '[', ']', '{', '}', '|']
cha = 838765592705237023
nu = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


@ client.event
async def on_message(message):
    global spe, cha, nu
    if message.content.startswith(""):
        mes = message.content[0:]
        now = datetime.datetime.now()
        now = int(now.strftime('%H'))
        now += 9
        if now >= 24:
            now = now - 24
        id = str(message.author.id)
        if id == '527500397645004800':
            f = open("wnsco.txt", "r")
            data = f.read()
            f.close()
            data = int(data) + 1
            f = open("wnsco.txt", "w")
            f.write(str(data))
            f.close()
            f = open("wnsxmr.txt", "r")
            data = f.readline()
            f.close()
            li1 = data.split(" ")
            for i in range(len(spe)):
                if spe[i] in mes:
                    li1[i] = str(int(li1[i]) + 1)
            f = open("wnsxmr.txt", "w")
            for i in range(len(li1)):
                if i <= 27:
                    text = li1[i] + " "
                    f.write(text)
                elif i == 28:
                    text = li1[i]
                    f.write(text)
            f.close()
            f = open("wnsdlf.txt", "r")
            data = f.read()
            f.close()
            data = data.split(" ")
            data[now] = str(int(data[now]) + 1)
            f = open("wnsdlf.txt", "w")
            for i in range(len(data)):
                if i <= 22:
                    ti1 = data[i] + " "
                    f.write(ti1)
                elif i == 23:
                    ti1 = data[i]
                    f.write(ti1)
            f.close()
            f = open("wnstn.txt", "r")
            data = f.read()
            f.close()
            data = data.split(" ")
            for i in range(len(mes)):
                if mes[i] in nu:
                    data[int(mes[i])] = str(int(data[int(mes[i])]) + 1)
            f = open("wnstn.txt", "w")
            for i in range(len(data)):
                if i <= 8:
                    tnt1 = data[i] + " "
                    f.write(tnt1)
                elif i == 9:
                    tnt1 = data[i]
                    f.write(tnt1)
            f.close()

        if id == '558169794646507541':
            f = open("dbco.txt", "r")
            data2 = f.read()
            f.close()
            data2 = int(data2) + 1
            f = open("dbco.txt", "w")
            f.write(str(data2))
            f.close()
            f = open("dbdlf.txt", "r")
            data2 = f.read()
            f.close()
            data2 = data2.split(" ")
            data2[now] = str(int(data2[now]) + 1)
            f = open("dbdlf.txt", "w")
            for i in range(len(data2)):
                if i <= 22:
                    ti2 = data2[i] + " "
                    f.write(ti2)
                elif i == 23:
                    ti2 = data2[i]
                    f.write(ti2)
            f.close()
            f = open("dbtn.txt", "r")
            data2 = f.read()
            f.close()
            data2 = data2.split(" ")
            for i in range(len(mes)):
                if mes[i] in nu:
                    data2[int(mes[i])] = str(int(data2[int(mes[i])]) + 1)
            f = open("dbtn.txt", "w")
            for i in range(len(data2)):
                if i <= 8:
                    tnt2 = data2[i] + " "
                    f.write(tnt2)
                elif i == 9:
                    tnt2 = data2[i]
                    f.write(tnt2)
            f.close()
            f = open("dbxmr.txt", "r")
            data2 = f.readline()
            f.close()
            li4 = data2.split(" ")
            for i in range(len(spe)):
                if spe[i] in mes:
                    li4[i] = str(int(li4[i]) + 1)
            f = open("dbxmr.txt", "w")
            for i in range(len(li4)):
                if i <= 27:
                    text2 = li4[i] + " "
                    f.write(text2)
                elif i == 28:
                    text2 = li4[i]
                    f.write(text2)
            f.close()

        if id == '404936174902444033':
            f = open("dnco.txt", "r")
            data3 = f.read()
            f.close()
            data3 = int(data3) + 1
            f = open("dnco.txt", "w")
            f.write(str(data3))
            f.close()
            f = open("dndlf.txt", "r")
            data3 = f.read()
            f.close()
            data3 = data3.split(" ")
            data3[now] = str(int(data3[now]) + 1)
            f = open("dndlf.txt", "w")
            for i in range(len(data3)):
                if i <= 22:
                    ti3 = data3[i] + " "
                    f.write(ti3)
                elif i == 23:
                    ti3 = data3[i]
                    f.write(ti3)
            f.close()
            f = open("dntn.txt", "r")
            data3 = f.read()
            f.close()
            data3 = data3.split(" ")
            for i in range(len(mes)):
                if mes[i] in nu:
                    data3[int(mes[i])] = str(int(data3[int(mes[i])]) + 1)
            f = open("dntn.txt", "w")
            for i in range(len(data3)):
                if i <= 8:
                    tnt3 = data3[i] + " "
                    f.write(tnt3)
                elif i == 9:
                    tnt3 = data3[i]
                    f.write(tnt3)
            f.close()
            f = open("dnxmr.txt", "r")
            data3 = f.readline()
            f.close()
            li6 = data3.split(" ")
            for i in range(len(spe)):
                if spe[i] in mes:
                    li6[i] = str(int(li6[i]) + 1)
            f = open("dnxmr.txt", "w")
            for i in range(len(li6)):
                if i <= 27:
                    text3 = li6[i] + " "
                    f.write(text3)
                elif i == 28:
                    text3 = li6[i]
                    f.write(text3)
            f.close()

        if id == '665823140915445760':
            f = open("tlco.txt", "r")
            data4 = f.read()
            f.close()
            data4 = int(data4) + 1
            f = open("tlco.txt", "w")
            f.write(str(data4))
            f.close()
            f = open("tldlf.txt", "r")
            data4 = f.read()
            f.close()
            data4 = data4.split(" ")
            data4[now] = str(int(data4[now]) + 1)
            f = open("tldlf.txt", "w")
            for i in range(len(data4)):
                if i <= 22:
                    ti4 = data4[i] + " "
                    f.write(ti4)
                elif i == 23:
                    ti4 = data4[i]
                    f.write(ti4)
            f.close()
            f = open("tltn.txt", "r")
            data4 = f.read()
            f.close()
            data4 = data4.split(" ")
            for i in range(len(mes)):
                if mes[i] in nu:
                    data4[int(mes[i])] = str(int(data4[int(mes[i])]) + 1)
            f = open("tltn.txt", "w")
            for i in range(len(data4)):
                if i <= 8:
                    tnt4 = data4[i] + " "
                    f.write(tnt4)
                elif i == 9:
                    tnt4 = data4[i]
                    f.write(tnt4)
            f.close()
            f = open("tlxmr.txt", "r")
            data4 = f.readline()
            f.close()
            li8 = data4.split(" ")
            for i in range(len(spe)):
                if spe[i] in mes:
                    li8[i] = str(int(li8[i]) + 1)
            f = open("tlxmr.txt", "w")
            for i in range(len(li8)):
                if i <= 27:
                    text4 = li8[i] + " "
                    f.write(text4)
                elif i == 28:
                    text4 = li8[i]
                    f.write(text4)
            f.close()

        if id == '503194657673707552':
            f = open("rbco.txt", "r")
            data5 = f.read()
            f.close()
            data5 = int(data5) + 1
            f = open("rbco.txt", "w")
            f.write(str(data5))
            f.close()
            f = open("rbdlf.txt", "r")
            data5 = f.read()
            f.close()
            data5 = data5.split(" ")
            data5[now] = str(int(data5[now]) + 1)
            f = open("rbdlf.txt", "w")
            for i in range(len(data5)):
                if i <= 22:
                    ti5 = data5[i] + " "
                    f.write(ti5)
                elif i == 23:
                    ti5 = data5[i]
                    f.write(ti5)
            f.close()
            f = open("rbtn.txt", "r")
            data5 = f.read()
            f.close()
            data5 = data5.split(" ")
            for i in range(len(mes)):
                if mes[i] in nu:
                    data5[int(mes[i])] = str(int(data5[int(mes[i])]) + 1)
            f = open("rbtn.txt", "w")
            for i in range(len(data5)):
                if i <= 8:
                    tnt5 = data5[i] + " "
                    f.write(tnt5)
                elif i == 9:
                    tnt5 = data5[i]
                    f.write(tnt5)
            f.close()
            f = open("rbxmr.txt", "r")
            data5 = f.readline()
            f.close()
            li10 = data5.split(" ")
            for i in range(len(spe)):
                if spe[i] in mes:
                    li10[i] = str(int(li10[i]) + 1)
            f = open("rbxmr.txt", "w")
            for i in range(len(li10)):
                if i <= 27:
                    text5 = li10[i] + " "
                    f.write(text5)
                elif i == 28:
                    text5 = li10[i]
                    f.write(text5)
            f.close()

        if id == '570836005989384212':
            f = open("ckdco.txt", "r")
            data6 = f.read()
            f.close()
            data6 = int(data6) + 1
            f = open("ckdco.txt", "w")
            f.write(str(data6))
            f.close()
            f = open("ckddlf.txt", "r")
            data6 = f.read()
            f.close()
            data6 = data6.split(" ")
            data6[now] = str(int(data6[now]) + 1)
            print(data6)
            f = open("ckddlf.txt", "w")
            for i in range(len(data6)):
                if i <= 22:
                    ti6 = data6[i] + " "
                    f.write(ti6)
                elif i == 23:
                    ti6 = data6[i]
                    f.write(ti6)
            f.close()
            f = open("ckdtn.txt", "r")
            data6 = f.read()
            f.close()
            data6 = data6.split(" ")
            for i in range(len(mes)):
                if mes[i] in nu:
                    data6[int(mes[i])] = str(int(data6[int(mes[i])]) + 1)
            f = open("ckdtn.txt", "w")
            for i in range(len(data6)):
                if i <= 8:
                    tnt6 = data6[i] + " "
                    f.write(tnt6)
                elif i == 9:
                    tnt6 = data6[i]
                    f.write(tnt6)
            f.close()
            f = open("ckdxmr.txt", "r")
            data6 = f.readline()
            f.close()
            li12 = data6.split(" ")
            for i in range(len(spe)):
                if spe[i] in mes:
                    li12[i] = str(int(li12[i]) + 1)
            f = open("ckdxmr.txt", "w")
            for i in range(len(li12)):
                if i <= 27:
                    text6 = li12[i] + " "
                    f.write(text6)
                elif i == 28:
                    text6 = li12[i]
                    f.write(text6)
            f.close()

        if id == '525201231790997505':
            f = open("wlco.txt", "r")
            data7 = f.read()
            f.close()
            data7 = int(data7) + 1
            f = open("wlco.txt", "w")
            f.write(str(data7))
            f.close()
            f = open("wldlf.txt", "r")
            data7 = f.read()
            f.close()
            data7 = data7.split(" ")
            data7[now] = str(int(data7[now]) + 1)
            f = open("wldlf.txt", "w")
            for i in range(len(data7)):
                if i <= 22:
                    ti7 = data7[i] + " "
                    f.write(ti7)
                elif i == 23:
                    ti7 = data7[i]
                    f.write(ti7)
            f.close()
            f = open("wltn.txt", "r")
            data7 = f.read()
            f.close()
            data7 = data7.split(" ")
            for i in range(len(mes)):
                if mes[i] in nu:
                    data7[int(mes[i])] = str(int(data7[int(mes[i])]) + 1)
            f = open("wltn.txt", "w")
            for i in range(len(data7)):
                if i <= 8:
                    tnt7 = data7[i] + " "
                    f.write(tnt7)
                elif i == 9:
                    tnt7 = data7[i]
                    f.write(tnt7)
            f.close()
            f = open("wlxmr.txt", "r")
            data7 = f.readline()
            f.close()
            li14 = data7.split(" ")
            for i in range(len(spe)):
                if spe[i] in mes:
                    li14[i] = str(int(li14[i]) + 1)
            f = open("wlxmr.txt", "w")
            for i in range(len(li14)):
                if i <= 27:
                    text7 = li14[i] + " "
                    f.write(text7)
                elif i == 28:
                    text7 = li14[i]
                    f.write(text7)
            f.close()

    if message.content.startswith("!채팅 정보 브루니"):
        f = open("wnsco.txt", "r")
        data = f.read()
        f.close()
        await message.channel.send("```채팅 횟수 : " + data + "```")
        f = open("wnsxmr.txt", "r")
        data = f.readline()
        f.close()
        li1 = data.split(" ")
        li3 = []
        for i in li1:
            li3.append(int(i))
        max1 = max(li3)
        index1 = li3.index(max1)
        special1 = spe[index1]
        await message.channel.send("```가장 많이친 특수기호 : " + special1 + "(" + str(max1) + "번)" + "```")
        f = open("wnsdlf.txt", "r")
        data = f.readline()
        f.close()
        data = data.split(" ")
        a = []
        for i in data:
            a.append(int(i))
        max1 = max(a)
        index1 = a.index(max1)
        await message.channel.send("```가장 활동량이 높은 시간대 : " + str(index1) + "시(" + str(max1) + "번)```")
        f = open("wnsvm.txt", "r")
        data = f.read()
        f.close()
        await message.channel.send("```프레드 사용 횟수 : " + data + "```")
        f = open("wnstn.txt", "r")
        data = f.read()
        f.close()
        data = data.split(" ")
        a = []
        for i in data:
            a.append(int(i))
        max1 = max(a)
        index1 = a.index(max1)
        await message.channel.send("```가장 많이친 숫자 : " + str(index1) + "(" + str(max1) + "번)```")

    if message.content.startswith("!채팅 정보 빼미요"):
        f = open("dbco.txt", "r")
        data2 = f.read()
        f.close()
        await message.channel.send("```채팅 횟수 : " + data2 + "```")
        f = open("dbxmr.txt", "r")
        data2 = f.readline()
        f.close()
        li4 = data2.split(" ")
        li5 = []
        for i in li4:
            li5.append(int(i))
        max2 = max(li5)
        index2 = li5.index(max2)
        special2 = spe[index2]
        await message.channel.send("```가장 많이친 특수기호 : " + special2 + "(" + str(max2) + "번)" + "```")
        f = open("dbdlf.txt", "r")
        data2 = f.readline()
        f.close()
        data2 = data2.split(" ")
        a2 = []
        for i in data2:
            a2.append(int(i))
        max2 = max(a2)
        index2 = a2.index(max2)
        await message.channel.send("```가장 활동량이 높은 시간대 : " + str(index2) + "시(" + str(max2) + "번)```")
        f = open("dbvm.txt", "r")
        data2 = f.read()
        f.close()
        await message.channel.send("```프레드 사용 횟수 : " + data2 + "```")
        f = open("dbtn.txt", "r")
        data2 = f.read()
        f.close()
        data2 = data2.split(" ")
        a2 = []
        for i in data2:
            a2.append(int(i))
        max2 = max(a2)
        index2 = a2.index(max2)
        await message.channel.send("```가장 많이친 숫자 : " + str(index2) + "(" + str(max2) + "번)```")

    if message.content.startswith("!채팅 정보 붸"):
        f = open("dnco.txt", "r")
        data3 = f.read()
        f.close()
        await message.channel.send("```채팅 횟수 : " + data3 + "```")
        f = open("dnvm.txt", "r")
        data3 = f.read()
        f.close()
        await message.channel.send("```프레드 사용 횟수 : " + data3 + "```")
        f = open("dndlf.txt", "r")
        data3 = f.readline()
        f.close()
        data3 = data3.split(" ")
        print(data3)
        a3 = []
        for i in data3:
            a3.append(int(i))
        max3 = max(a3)
        index3 = a3.index(max3)
        await message.channel.send("```가장 활동량이 높은 시간대 : " + str(index3) + "시(" + str(max3) + "번)```")
        f = open("dntn.txt", "r")
        data3 = f.read()
        f.close()
        data3 = data3.split(" ")
        a3 = []
        for i in data3:
            a3.append(int(i))
        max3 = max(a3)
        index3 = a3.index(max3)
        await message.channel.send("```가장 많이친 숫자 : " + str(index3) + "(" + str(max3) + "번)```")
        f = open("dnxmr.txt", "r")
        data3 = f.readline()
        f.close()
        li6 = data3.split(" ")
        li7 = []
        for i in li6:
            li7.append(int(i))
        max3 = max(li7)
        index3 = li7.index(max3)
        special3 = spe[index3]
        await message.channel.send("```가장 많이친 특수기호 : " + special3 + "(" + str(max3) + "번)" + "```")

    if message.content.startswith("!채팅 정보 레게노치킨"):
        f = open("tlco.txt", "r")
        data4 = f.read()
        f.close()
        await message.channel.send("```채팅 횟수 : " + data4 + "```")
        f = open("tlxmr.txt", "r")
        data4 = f.readline()
        f.close()
        li8 = data4.split(" ")
        li9 = []
        for i in li8:
            li9.append(int(i))
        max4 = max(li9)
        index4 = li9.index(max4)
        special4 = spe[index4]
        await message.channel.send("```가장 많이친 특수기호 : " + special4 + "(" + str(max4) + "번)" + "```")
        f = open("tldlf.txt", "r")
        data4 = f.readline()
        f.close()
        data4 = data4.split(" ")
        a4 = []
        for i in data4:
            a4.append(int(i))
        max4 = max(a4)
        index4 = a4.index(max4)
        await message.channel.send("```가장 활동량이 높은 시간대 : " + str(index4) + "시(" + str(max4) + "번)```")
        f = open("tlvm.txt", "r")
        data4 = f.read()
        f.close()
        await message.channel.send("```프레드 사용 횟수 : " + data4 + "```")
        f = open("tltn.txt", "r")
        data4 = f.read()
        f.close()
        data4 = data4.split(" ")
        a4 = []
        for i in data4:
            a4.append(int(i))
        max4 = max(a4)
        index4 = a4.index(max4)
        await message.channel.send("```가장 많이친 숫자 : " + str(index4) + "(" + str(max4) + "번)```")

    if message.content.startswith("!채팅 정보 포션"):
        f = open("rbco.txt", "r")
        data5 = f.read()
        f.close()
        await message.channel.send("```채팅 횟수 : " + data5 + "```")
        f = open("rbvm.txt", "r")
        data5 = f.read()
        f.close()
        await message.channel.send("```프레드 사용 횟수 : " + data5 + "```")
        f = open("rbdlf.txt", "r")
        data5 = f.readline()
        f.close()
        data5 = data5.split(" ")
        a5 = []
        for i in data5:
            a5.append(int(i))
        max5 = max(a5)
        index5 = a5.index(max5)
        await message.channel.send("```가장 활동량이 높은 시간대 : " + str(index5) + "시(" + str(max5) + "번)```")
        f = open("rbtn.txt", "r")
        data5 = f.read()
        f.close()
        data5 = data5.split(" ")
        a5 = []
        for i in data5:
            a5.append(int(i))
        max5 = max(a5)
        index5 = a5.index(max5)
        await message.channel.send("```가장 많이친 숫자 : " + str(index5) + "(" + str(max5) + "번)```")
        f = open("rbxmr.txt", "r")
        data5 = f.readline()
        f.close()
        li10 = data5.split(" ")
        li11 = []
        for i in li10:
            li11.append(int(i))
        max5 = max(li11)
        index5 = li11.index(max5)
        special5 = spe[index5]
        await message.channel.send("```가장 많이친 특수기호 : " + special5 + "(" + str(max5) + "번)" + "```")

    if message.content.startswith("!채팅 정보 창빈"):
        f = open("ckdco.txt", "r")
        data6 = f.read()
        f.close()
        await message.channel.send("```채팅 횟수 : " + data6 + "```")
        f = open("ckddlf.txt", "r")
        data6 = f.readline()
        f.close()
        data6 = data6.split(" ")
        print(data6)
        a6 = []
        for i in data6:
            a6.append(int(i))
        max6 = max(a6)
        index6 = a6.index(max6)
        await message.channel.send("```가장 활동량이 높은 시간대 : " + str(index6) + "시(" + str(max6) + "번)```")
        f = open("ckdtn.txt", "r")
        data6 = f.read()
        f.close()
        data6 = data6.split(" ")
        a6 = []
        for i in data6:
            a6.append(int(i))
        max6 = max(a6)
        index6 = a6.index(max6)
        await message.channel.send("```가장 많이친 숫자 : " + str(index6) + "(" + str(max6) + "번)```")
        f = open("ckdxmr.txt", "r")
        data6 = f.readline()
        f.close()
        li12 = data6.split(" ")
        li13 = []
        for i in li12:
            li13.append(int(i))
        max6 = max(li13)
        index6 = li13.index(max6)
        special6 = spe[index6]
        await message.channel.send("```가장 많이친 특수기호 : " + special6 + "(" + str(max6) + "번)" + "```")

    if message.content.startswith("!채팅 정보 지소"):
        f = open("wlco.txt", "r")
        data7 = f.read()
        f.close()
        await message.channel.send("```채팅 횟수 : " + data7 + "```")
        f = open("wldlf.txt", "r")
        data7 = f.readline()
        f.close()
        data7 = data7.split(" ")
        a7 = []
        for i in data7:
            a7.append(int(i))
        max7 = max(a7)
        index7 = a7.index(max7)
        await message.channel.send("```가장 활동량이 높은 시간대 : " + str(index7) + "시(" + str(max7) + "번)```")
        f = open("wltn.txt", "r")
        data7 = f.read()
        f.close()
        data7 = data7.split(" ")
        a7 = []
        for i in data7:
            a7.append(int(i))
        max7 = max(a7)
        index7 = a7.index(max7)
        await message.channel.send("```가장 많이친 숫자 : " + str(index7) + "(" + str(max7) + "번)```")
        f = open("wlxmr.txt", "r")
        data7 = f.readline()
        f.close()
        li14 = data7.split(" ")
        li15 = []
        for i in li14:
            li15.append(int(i))
        max7 = max(li15)
        index7 = li15.index(max7)
        special7 = spe[index7]
        await message.channel.send("```가장 많이친 특수기호 : " + special7 + "(" + str(max7) + "번)" + "```")

    if message.content.startswith(";;p"):
        id = str(message.author.id)
        if id == '527500397645004800':
            f = open("wnsvm.txt", "r")
            data = f.read()
            f.close()
            data = int(data) + 1
            f = open("wnsvm.txt", "w")
            f.write(str(data))
            f.close()
        if id == '558169794646507541':
            f = open("dbvm.txt", "r")
            data2 = f.read()
            f.close()
            data2 = int(data2) + 1
            f = open("dbvm.txt", "w")
            f.write(str(data2))
            f.close()
        if id == '404936174902444033':
            f = open("dnvm.txt", "r")
            data3 = f.read()
            f.close()
            data3 = int(data3) + 1
            f = open("dnvm.txt", "w")
            f.write(str(data3))
            f.close()
        if id == '665823140915445760':
            f = open("tlvm.txt", "r")
            data4 = f.read()
            f.close()
            data4 = int(data4) + 1
            f = open("tlvm.txt", "w")
            f.write(str(data4))
            f.close()
        if id == '503194657673707552':
            f = open("rbvm.txt", "r")
            data5 = f.read()
            f.close()
            data5 = int(data5) + 1
            f = open("rbvm.txt", "w")
            f.write(str(data5))
            f.close()

    if message.content.startswith(""):
        mes2 = message.content[0:]
        botname = message.author.name
        if botname == '브리루이니 ver2.4':
            pass
        elif botname != '브리루이니 ver2.4':
            await client.get_channel(int(cha)).send(botname + " : " + mes2)


client.run("ODM4MDc2ODcxMTI3MjAzOTAy.YI116A.aACQ9cebi8CFUHBgwTwu6s0PMA4")
