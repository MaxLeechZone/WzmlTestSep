#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '<tg-emoji emoji-id="5305398381479209877">💀</tg-emoji> Owner'
    ST_BN1_URL = 'https://t.me/PROFE07XH'
    ST_BN2_NAME = 'Update'
    ST_BN2_URL = 'https://t.me/Max_Leech_Zone_Update'
    ST_MSG = '''<pre><b>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.Type {help_command} to get a list of available commands</b></pre>'''
    ST_BOTPM = '''<pre><i>Now, This bot will send all your files and links here. Start Using ...</pre></i>'''
    ST_UNAUTH = '''<pre><i>You Are not authorized user!</i></pre>'''
    OWN_TOKEN_GENERATE = '''<pre><b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i></pre>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<pre><b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i></pre>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token🗽'
    TOKEN_MSG = '''<pre><b><u>Generated Temporary Login Token!</u></b></pre>
<pre><b>Temp Token:</b></pre> <code>{token}</code>
<pre><b>Validity:</b></pre> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = 'Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<pre><b>Already Bot Login In!</b></pre>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "<pre>🚨 <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b></pre>"

    # async def stats(client, message):
    BOT_STATS = '''<pre expandable><tg-emoji emoji-id="5305457750812142209">💀</tg-emoji> <b><i>BOT STATISTICS :</i></b>
<b>Bot Uptime :</b> {bot_uptime}

<b><i>RAM ( MEMORY ) :</i></b>
{ram_bar} {ram}%
<b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

<b><i>SWAP MEMORY :</i></b>
{swap_bar} {swap}%
<b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

<b><i>DISK :</i></b>
{disk_bar} {disk}%
<b>Total Disk Read :</b> {disk_read}
<b>Total Disk Write :</b> {disk_write}
<b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}</pre>
    
    '''
    SYS_STATS = '''<pre expandable><tg-emoji emoji-id="5305439935287798580">💀</tg-emoji> <b><i>OS SYSTEM :</i></b>
<b>OS Uptime :</b> {os_uptime}
<b>OS Version :</b> {os_version}
<b>OS Arch :</b> {os_arch}

🛜 <b><i>NETWORK STATS :</i></b>
<b>Upload Data:</b> {up_data}
<b>Download Data:</b> {dl_data}
<b>Pkts Sent:</b> {pkt_sent}k
<b>Pkts Received:</b> {pkt_recv}k
<b>Total I/O Data:</b> {tl_data}

<b>CPU :</b>
{cpu_bar} {cpu}%
<b>CPU Frequency :</b> {cpu_freq}
<b>System Avg Load :</b> {sys_load}
<b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
<b>Total Core(s) :</b> {total_core}
<b>Usable CPU(s) :</b> {cpu_use}</pre>
    '''
    REPO_STATS = '''<pre><tg-emoji emoji-id="5305346030122838661">💀</tg-emoji> <b><i>REPO STATISTICS :</i></b>
<b>Bot Updated :</b> {last_commit}
<b>Current Version :</b> {bot_version}
<b>Latest Version :</b> {lat_version}
<b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code></pre>
    '''
    BOT_LIMITS = '''<pre expandable><tg-emoji emoji-id="5305615642399877091">💀</tg-emoji> <b><i>BOT LIMITATIONS :</i></b>
<b>Direct Limit :</b> {DL} GB
<b>Torrent Limit :</b> {TL} GB
<b>GDrive Limit :</b> {GL} GB
<b>YT-DLP Limit :</b> {YL} GB
<b>Playlist Limit :</b> {PL}
<b>Mega Limit :</b> {ML} GB
<b>Clone Limit :</b> {CL} GB
<b>Leech Limit :</b> {LL} GB

<b>Token Validity :</b> {TV}
<b>User Time Limit :</b> {UTI} / task
<b>User Parallel Tasks :</b> {UT}
<b>Bot Parallel Tasks :</b> {BT}</pre>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<pre><i>Restarting...</i></pre>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<pre><tg-emoji emoji-id="5305284861198610544">💀</tg-emoji> <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}</pre>'''
    RESTARTED = '''<pre><tg-emoji emoji-id="5305281906261110448">💀</tg-emoji> <b><i>Bot Restarted!</i></b></pre>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<pre><i>Starting Ping..</i></pre>'
    PING_VALUE = '<pre><b>Tunik🐾</b>\n<code>{value} ms..</code></pre>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<pre><b><i>Task Started</i></b>
<b>Mode:</b> {Mode}
<b>By:</b> {Tag}\n\n</pre>"""
    LINKS_SOURCE = """<pre>➲ <b>Source:</b>
<b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n</pre>"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "<pre>➲ <b><u>Task Started :</u></b>\n┃\n┖ <b>Link:</b> <a href='{msg_link}'>Click Here</a></pre>"
    L_LOG_START =           "<pre>➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>Click Here</a></pre>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n┃\n'
    SIZE =                  '<tg-emoji emoji-id="5305750555912579213">💀</tg-emoji> ┠ <b>Size: </b>{Size}\n'
    ELAPSE =                '<tg-emoji emoji-id="5305714357928210941">💀</tg-emoji> ┠ <b>Elapsed: </b>{Time}\n'
    MODE =                  '<tg-emoji emoji-id="5305368548636370953">💀</tg-emoji> ┠ <b>Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<tg-emoji emoji-id="5305278487467141049">💀</tg-emoji> ┠ <b>Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '<tg-emoji emoji-id="5305406851154717270">💀</tg-emoji> ┠ <b>Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '<tg-emoji emoji-id="5307672790000740780">💀</tg-emoji> ┠ <b>By: </b>{Tag}\n\n'
    PM_BOT_MSG =            '<tg-emoji emoji-id="5307845791283423615">💀</tg-emoji> ➲ <b><i>File(s) have been Sent above</i></b>'
    L_BOT_MSG =             '<tg-emoji emoji-id="5305509492283158466">💀</tg-emoji> ➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '<tg-emoji emoji-id="5305242779109042877">💀</tg-emoji> ➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '<tg-emoji emoji-id="5305262699167361655">💀</tg-emoji> ┠<b>Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '<tg-emoji emoji-id="5305615002449752274">💀</tg-emoji> ┠<b>SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠<b>Files: </b>{Files}\n'
    RCPATH =                '<tg-emoji emoji-id="5305312447773551777">💀</tg-emoji> ┠<b>Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '<tg-emoji emoji-id="5305533204797598593">💀</tg-emoji> ┠<b>By: </b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<pre expandable><code><i>{Name}</i></code></pre>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '<pre>{Bar}</pre>'
    PROCESSED =         '<tg-emoji emoji-id="5305654984300309922">💀</tg-emoji> \n┠ <b>Processed:</b> {Processed}'
    STATUS =            '<tg-emoji emoji-id="5305725344454550767">💀</tg-emoji> \n┠ <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> {Eta}'
    SPEED =             '<tg-emoji emoji-id="5305598007264160685">💀</tg-emoji> \n┠ <b>Speed:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '<tg-emoji emoji-id="5305727771111075113">💀</tg-emoji> \n┠ <b>Engine:</b> {Engine}'
    STA_MODE =          '<tg-emoji emoji-id="5305600829057674165">💀</tg-emoji> \n┠ <b>Mode:</b> {Mode}'
    SEEDERS =           '\n┠ <b>Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '<tg-emoji emoji-id="5305730824832823212">💀</tg-emoji> \n┠ <b>Size: </b>{Size}'
    SEED_SPEED =     '<tg-emoji emoji-id="5307688217523269612">💀</tg-emoji> \n┠ <b>Speed: </b> {Speed} | '
    UPLOADED =                                     '<tg-emoji emoji-id="5305548065384442487">💀</tg-emoji> <b>Uploaded: </b> {Upload}'
    RATIO =          '<tg-emoji emoji-id="5305697272548306072">💀</tg-emoji> \n┠ <b>Ratio: </b> {Ratio} | '
    TIME =                                         '<tg-emoji emoji-id="5308020270034855416">💀</tg-emoji> <b>Time: </b> {Time}'
    SEED_ENGINE =    '<tg-emoji emoji-id="5305540072450304906">💀</tg-emoji> \n┠ <b>Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '<tg-emoji emoji-id="5307899783317300730">💀</tg-emoji> \n┠ <b>Size: </b>{Size}'
    NON_ENGINE =     '<tg-emoji emoji-id="5305597139680766780">💀</tg-emoji> \n┠ <b>Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b>User:</b> <code>{User}</code> | '
    ID =                                                        '<b>ID:</b> <code>{Id}</code>'
    BTSEL =          '\n┠ <b>Select:</b> {Btsel}'
    CANCEL =         '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '<tg-emoji emoji-id="5305417013047339185">💀</tg-emoji> ⌬ <b><i>Bot Stats</i></b>\n'
    TASKS =  '┠ <b>Tasks:</b> {Tasks}\n'
    BOT_TASKS = '┠ <b>Tasks:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n'
    Cpu = '┠ <b>CPU:</b> {cpu}% | '
    FREE =                      '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n┠ <b>RAM:</b> {ram}% | '
    uptime =                     '<b>UPTIME:</b> {uptime}'
    DL = '\n┖ <b>DL:</b> {DL}/s | '
    UL =                        '<b>UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '☚'
    REFRESH = ' MᴀxBᴏᴛꜱ\n{Page}'
    NEXT = '☛'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '┠<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '┠<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠<b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠<b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠<b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠<b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┠<b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<pre><i>No Active Downloads!</i>
    
<b><i>Bot Stats</i></b>
<b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
<b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}</pre>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''<pre><tg-emoji emoji-id="5305397750119019510">💀</tg-emoji><b><u>User Settings :</u></b>
        
<b> Name :</b> {NAME} ( <code>{ID}</code> )
<b> Username :</b> {USERNAME}
<b> Telegram DC :</b> {DC}
<b> Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg</pre>'''

    UNIVERSAL = '''<pre><tg-emoji emoji-id="5305352343724764854">💀</tg-emoji> <b><u>Universal Settings : {NAME}</u></b>

<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
<b> Daily Tasks :</b> <code>{DT}</code> per day
<b> Last Bot Used :</b> <code>{LAST_USED}</code>
<b> User Session :</b> <code>{USESS}</code>
<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
<b> Save Mode :</b> <code>{SAVE_MODE}</code>
<b> User Bot PM :</b> <code>{BOT_PM}</code></pre>'''

    MIRROR = '''<pre><tg-emoji emoji-id="5305242259418000534">💀</tg-emoji> <b><u>Mirror/Clone Settings : {NAME}</u></b>

<b> RClone Config :</b> <i>{RCLONE}</i>
<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
<b> Mirror Remname :</b> <code>{MREMNAME}</code>
<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
<b> User TD Mode :</b> <i>{TMODE}</i>
<b> Total User TD(s) :</b> <i>{USERTD}</i>
<b> Daily Mirror :</b> <code>{DM}</code> per day</pre>'''

    LEECH = '''<pre expandable><tg-emoji emoji-id="5305661242067659565">💀</tg-emoji> <b><u>Leech Settings for {NAME}</u></b>

<b> Daily Leech : </b><code>{DL}</code> per day
<b> Leech Type :</b> <i>{LTYPE}</i>
<b> Custom Thumbnail :</b> <i>{THUMB}</i>
<b> Auto Poster :</b> <i>{AUTOTHUMB}</i>
<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
<b> Leech Caption :</b> <code>{LCAPTION}</code>
<b> Leech Prefix :</b> <code>{LPREFIX}</code>
<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
<b> Leech Dumps :</b> <code>{LDUMP}</code>
<b> Leech Remname :</b> <code>{LREMNAME}</code></pre>'''

