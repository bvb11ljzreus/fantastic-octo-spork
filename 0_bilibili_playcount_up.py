from selenium.webdriver.firefox.webdriver import WebDriver
import selelib
from collections import defaultdict

def work(_driver: WebDriver, args):
    import sys
    import ml
    import time
    import selelib
    print('work start ')
    ml.ensure_dir('screenshots')
    ml.ensure_dir('bili')
    # frehit
    _driver.get(args)
    # 旧xpath，已经失效
    # xpath = '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[10]/div[2]/div[2]/div[1]/div[1]/button'
    # xpath = '/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[11]/div[2]/div[2]/div[1]/div[1]/button'
    xpath='/html/body/div[2]/div[4]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[11]/div[2]/div[2]/div[1]/div[2]/div/span[1]'
    selelib.lib(_driver).wait_until_xpath(xpath,timeout=3)
    # print('html_code ... \n',selelib.lib(_driver).get_html())

    # return 0
    # time.sleep(20)
    
    print('button ok........')
    time.sleep(3)
    print('before exec')
    # _driver.execute_script('''
    # function click(x,y){
    # var ev = document.createEvent("MouseEvent");
    # var el = document.elementFromPoint(x,y);
    # ev.initMouseEvent(
    #     "click",
    #     true, true,
    #     window, null,
    #     x, y, 0, 0,
    #     false, false, false, false,
    #     0 , null
    # );
    # el.dispatchEvent(ev);
    # } 
    # click(200,200);
    # ''')
    x = selelib.lib(_driver).findall(r'总播放数\d+')
    print(x)
    ml.write_string_append('bili/count.txt', ml.time_() + " " + str(x) + '\n')
    selelib.lib(_driver).screen_shot('screenshots/bilibili播放量up_播放前.png')
    time.sleep(7)
    selelib.lib(_driver).screen_shot('screenshots/bilibili播放量up_播放10秒后.png')
    return 1


if __name__ == '__main__':
    import quick_firefox
    import ml
    import time
    start=time.time()
    videos=['https://www.bilibili.com/video/BV1gP4y1V73n']
    counter=0
    failure=defaultdict(lambda:None)
    while counter<60:
        r = quick_firefox.run_sync(work=work, args=(videos[counter%len(videos)]))
        
        if not r:
            if failure[videos[counter%len(videos)]]:
                failure[videos[counter%len(videos)]]+=1
            else:
                failure[videos[counter%len(videos)]]=1
        # assert r,videos[counter%len(videos)]+str(' error')
        
        if time.time()-start>5*60*60:
        # if time.time()-start>90:
            break
        counter+=1
    print('run success')

    print('collected failure dict : ',failure)
