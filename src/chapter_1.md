# Chapter 1
ZAP Scanning Report Login

ZAP Scanning Report Login
=========================

Generated with [![The ZAP logo](2024-01-07-ZAP-Report-Login/zap32x32.png)ZAP](https://zaproxy.org) on Sun 7 Jan 2024, at 20:32:27

ZAP Version: 2.14.0

Contents
--------

1.  [About this report](#about-this-report)
    1.  [Report parameters](#report-parameters)
*   [Summaries](#summaries)
    1.  [Alert counts by risk and confidence](#risk-confidence-counts)
    2.  [Alert counts by site and risk](#site-risk-counts)
    3.  [Alert counts by alert type](#alert-type-counts)
*   [Alerts](#alerts)
    1.  [Risk\=Medium, Confidence\=High (1)](#alerts--risk-2-confidence-3)
    2.  [Risk\=Medium, Confidence\=Medium (1)](#alerts--risk-2-confidence-2)
    3.  [Risk\=Low, Confidence\=High (2)](#alerts--risk-1-confidence-3)
    4.  [Risk\=Informational, Confidence\=High (1)](#alerts--risk-0-confidence-3)
*   [Appendix](#appendix)
    1.  [Alert types](#alert-types)

About this report
-----------------

### Report parameters

#### Contexts

No contexts were selected, so all contexts were included by default.

#### Sites

The following sites were included:

*   https://contile.services.mozilla.com
*   https://safebrowsing.googleapis.com
*   https://incoming.telemetry.mozilla.org
*   https://api.qa.permate.com

(If no sites were selected, all sites were included by default.)

An included site must also be within one of the included contexts for its data to be included in the report.

#### Risk levels

Included: High, Medium, Low, Informational

Excluded: None

#### Confidence levels

Included: User Confirmed, High, Medium, Low

Excluded: User Confirmed, High, Medium, Low, False Positive

Summaries
---------

### Alert counts by risk and confidence

This table shows the number of alerts for each level of risk and confidence included in the report.

(The percentages in brackets represent the count as a percentage of the total number of alerts included in the report, rounded to one decimal place.)



Confidence

User Confirmed

High

Medium

Low

Total

Risk

High

0  
(0.0%)

0  
(0.0%)

0  
(0.0%)

0  
(0.0%)

0  
(0.0%)

Medium

0  
(0.0%)

1  
(20.0%)

1  
(20.0%)

0  
(0.0%)

2  
(40.0%)

Low

0  
(0.0%)

2  
(40.0%)

0  
(0.0%)

0  
(0.0%)

2  
(40.0%)

Informational

0  
(0.0%)

1  
(20.0%)

0  
(0.0%)

0  
(0.0%)

1  
(20.0%)

Total

0  
(0.0%)

4  
(80.0%)

1  
(20.0%)

0  
(0.0%)

5  
(100%)

### Alert counts by site and risk

This table shows, for each site for which one or more alerts were raised, the number of alerts raised at each risk level.

Alerts with a confidence level of "False Positive" have been excluded from these counts.

(The numbers in brackets are the number of alerts raised for the site at or above that risk level.)



Risk

High  
(= High)

Medium  
(>= Medium)

Low  
(>= Low)

Informational  
(>= Informational)

Site

https://safebrowsing.googleapis.com

0  
(0)

0  
(0)

1  
(1)

0  
(1)

https://api.qa.permate.com

0  
(0)

2  
(2)

1  
(3)

1  
(4)

### Alert counts by alert type

This table shows the number of alerts of each alert type, together with the alert type's risk level.

(The percentages in brackets represent each count as a percentage, rounded to one decimal place, of the total number of alerts included in this report.)

Alert type

Risk

Count

[Content Security Policy (CSP) Header Not Set](#alert-type-0)

Medium

2  
(40.0%)

[Cross-Domain Misconfiguration](#alert-type-1)

Medium

6  
(120.0%)

[Server Leaks Version Information via "Server" HTTP Response Header Field](#alert-type-2)

Low

1  
(20.0%)

[Strict-Transport-Security Header Not Set](#alert-type-3)

Low

9  
(180.0%)

[Authentication Request Identified](#alert-type-4)

Informational

1  
(20.0%)

Total

5

Alerts
------

1.  ### Risk\=Medium, Confidence\=High (1)

    1.  #### https://api.qa.permate.com (1)

        1.  ##### [Content Security Policy (CSP) Header Not Set](#alert-type-0) (1)

            1.  OPTIONS https://api.qa.permate.com/v1/auth/login

                Alert tags

                *   [OWASP\_2021\_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
                *   [OWASP\_2017\_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)

                Alert description

                Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

                Request

                Request line and header section (484 bytes)

                    OPTIONS https://api.qa.permate.com/v1/auth/login HTTP/1.1
                    host: api.qa.permate.com
                    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
                    Accept: */*
                    Accept-Language: en-US,en;q=0.5
                    Access-Control-Request-Method: POST
                    Access-Control-Request-Headers: content-type
                    Referer: https://qa.permate.com/
                    Origin: https://qa.permate.com
                    DNT: 1
                    Connection: keep-alive
                    Sec-Fetch-Dest: empty
                    Sec-Fetch-Mode: cors
                    Sec-Fetch-Site: same-site

                Request body (0 bytes)

                Response

                Status line and header section (659 bytes)

                    HTTP/1.1 200 OK
                    Date: Sun, 07 Jan 2024 13:17:37 GMT
                    Content-Type: text/html; charset=utf-8
                    Content-Length: 0
                    Connection: keep-alive
                    x-amzn-RequestId: 897d8054-e663-4753-b98c-e0caab7d94a2
                    Access-Control-Allow-Origin: https://qa.permate.com
                    Allow: OPTIONS, POST
                    Access-Control-Allow-Headers: content-type
                    x-amzn-Remapped-Content-Length: 0
                    x-amzn-Remapped-Connection: keep-alive
                    x-amz-apigw-id: RK6huHjsoAMED7w=
                    Vary: Origin
                    x-amzn-Remapped-Server: gunicorn
                    Access-Control-Allow-Methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
                    X-Amzn-Trace-Id: Root=1-659aa471-7351f5966b9f1cdc578040d7
                    x-amzn-Remapped-Date: Sun, 07 Jan 2024 13:17:37 GMT

                Response body (0 bytes)

                Solution

                Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

2.  ### Risk\=Medium, Confidence\=Medium (1)

    1.  #### https://api.qa.permate.com (1)

        1.  ##### [Cross-Domain Misconfiguration](#alert-type-1) (1)

            1.  GET https://api.qa.permate.com

                Alert tags

                *   [OWASP\_2021\_A01](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)
                *   [OWASP\_2017\_A05](https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control.html)

                Alert description

                Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server

                Other info

                The CORS misconfiguration on the web server permits cross-domain read requests from arbitrary third party domains, using unauthenticated APIs on this domain. Web browser implementations do not permit arbitrary third parties to read the response from authenticated APIs, however. This reduces the risk somewhat. This misconfiguration could be used by an attacker to access data that is available in an unauthenticated manner, but which uses some other form of security, such as IP address white-listing.

                Request

                Request line and header section (204 bytes)

                    GET https://api.qa.permate.com HTTP/1.1
                    host: api.qa.permate.com
                    user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0
                    pragma: no-cache
                    cache-control: no-cache

                Request body (0 bytes)

                Response

                Status line and header section (532 bytes)

                    HTTP/1.1 403 Forbidden
                    Date: Sun, 07 Jan 2024 13:17:54 GMT
                    Content-Type: application/json
                    Content-Length: 42
                    Connection: keep-alive
                    x-amzn-RequestId: 7dd0de06-fef1-45bb-9f45-9bc6c229b771
                    Access-Control-Allow-Origin: *
                    Access-Control-Allow-Headers: Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,cache-control
                    x-amzn-ErrorType: MissingAuthenticationTokenException
                    x-amz-apigw-id: RK6kfH2EIAMETSA=
                    Access-Control-Allow-Methods: GET,OPTIONS
                    X-Amzn-Trace-Id: Root=1-659aa482-7c79597d70a9241d68d986f1

                Response body (42 bytes)

                    {"message":"Missing Authentication Token"}

                Evidence

                    Access-Control-Allow-Origin: *

                Solution

                Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).

                Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

3.  ### Risk\=Low, Confidence\=High (2)

    1.  #### https://safebrowsing.googleapis.com (1)

        1.  ##### [Server Leaks Version Information via "Server" HTTP Response Header Field](#alert-type-2) (1)

            1.  GET https://safebrowsing.googleapis.com/v4/threatListUpdates:fetch?$ct=application/x-protobuf&key=AIzaSyC7jsptDS3am4tPx4r3nxis7IMjBc5Dovo&$httpMethod=POST&$req=ChUKE25hdmNsaWVudC1hdXRvLWZmb3gaJwgFEAQaGwoNCAUQBhgBIgMwMDEwARDJ0hQaAhgEmV4lZCICIAIoARonCAEQBBobCg0IARAGGAEiAzAwMTABEIHTDRoCGAQhpkbvIgIgAigBGicIAxAEGhsKDQgDEAYYASIDMDAxMAEQtMoNGgIYBFA9rpIiAiACKAEaJwgHEAQaGwoNCAcQBhgBIgMwMDEwARC6mQ4aAhgElRt0KiICIAIoARolCAkQBBoZCg0ICRAGGAEiAzAwMTABECMaAhgE5WKYUCICIAIoAQ==

                Alert tags

                *   [OWASP\_2021\_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
                *   [OWASP\_2017\_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)
                *   [WSTG-v42-INFO-02](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)

                Alert description

                The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

                Request

                Request line and header section (826 bytes)

                    GET https://safebrowsing.googleapis.com/v4/threatListUpdates:fetch?$ct=application/x-protobuf&key=AIzaSyC7jsptDS3am4tPx4r3nxis7IMjBc5Dovo&$httpMethod=POST&$req=ChUKE25hdmNsaWVudC1hdXRvLWZmb3gaJwgFEAQaGwoNCAUQBhgBIgMwMDEwARDJ0hQaAhgEmV4lZCICIAIoARonCAEQBBobCg0IARAGGAEiAzAwMTABEIHTDRoCGAQhpkbvIgIgAigBGicIAxAEGhsKDQgDEAYYASIDMDAxMAEQtMoNGgIYBFA9rpIiAiACKAEaJwgHEAQaGwoNCAcQBhgBIgMwMDEwARC6mQ4aAhgElRt0KiICIAIoARolCAkQBBoZCg0ICRAGGAEiAzAwMTABECMaAhgE5WKYUCICIAIoAQ== HTTP/1.1
                    host: safebrowsing.googleapis.com
                    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
                    Accept: */*
                    Accept-Language: en-US,en;q=0.5
                    X-HTTP-Method-Override: POST
                    Connection: close
                    DNT: 1
                    Sec-Fetch-Dest: empty
                    Sec-Fetch-Mode: no-cors
                    Sec-Fetch-Site: none
                    Pragma: no-cache
                    Cache-Control: no-cache

                Request body (0 bytes)

                Response

                Status line and header section (367 bytes)

                    HTTP/1.1 200 OK
                    Vary: Accept-Encoding
                    Content-Type: application/x-protobuf
                    Content-Disposition: attachment
                    Date: Sun, 07 Jan 2024 13:29:08 GMT
                    Server: scaffolding on HTTPServer2
                    Content-Length: 8427
                    X-XSS-Protection: 0
                    X-Frame-Options: SAMEORIGIN
                    X-Content-Type-Options: nosniff
                    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
                    Connection: close

                Response body (8427 bytes)


                    5 *%"û$Ôï¬÷"î$z.º|Âª'/êÆ?=»ÃÔÓ"£ë@'\Íïºÿnq@/öñ¬´
                    ¯#A£´¿+äÀe5yb4Ô/Ý kaÙg'Ì88ÉD<Æ
                    YHUÞã&SgÏ\Î	¨|!¾Øe¸òÜyjùð;zzgR"{É\Êü6¼¡øuñ]½ªW©ZCúr¸~ò9G¤'*ø¼A\MË/ØÉV 8qiº+ôÚ¨zÅQ[£#°°ý°~ï¨´<¤GÒt
                    ]pðFÈ@Ç¦Á5&R®½A¨j`ý¤[§ñÂ»Vøål¢Xx,
                    Fì,öÚ­0ÇLã°þ¨|:¸#bYÍ#­°T|ñæ{;£(t`sé9ÿÆ#RëÕ £Ây. :òkàÙG§;;©Ð³kòÕlatÓå~î½±÷
                    
                    Äw^A]#ÚnteÅðV¤¯ËJ~Eÿ!µÌÕÚfåíAóñ­jª±Öñwuìûë$;eEáòts'PbØÆ³8¹å±£®Yc=s])É´­®t°¡S;÷§Ôì×É®Ò'±(?ì2ÒÈ,bè«]¬ïÒäè0óèÔl÷åa	æ`*#c±I.Þt_ÕUå¾S"r¸\Ö+ÙÍõGG2£.PÊ~äÚó=fðH©6cÅÀ'ãø¢>áð²_0w¹ô<ß
                    jeD^3o«êxïD þØZÈÛ¡W|Þë!ÅÓlÃe²èrìF(x0-$\7ù¦Æj 9¤"kdÌÆk`>¯ç]æÎØkN¾"°s,>¯yJ¶PR6_,ÄÀ1Ð43ôý^1Ý¿$ÖÙgEô\j+ÖvË]ÊH:ð<ü×á°
                    ¦÷ç4ðÐÃB-
                    	ß¦m»\@2é.Jö'îÊÎæNçwîö±jt¬Å?.ÐTqw]î.Ñ`.Û}N;$*bi¢å=ºi¿ðWF 9ÂÞ¥÷9xì¿64üjJP´ñjJÛBx;6¬9å»>¢Òv;Òo[+²'
                    0kM
                    v¡+ÙhqÈ|mk?6ÎòcrèÁ
                    /§Ý·ükv»ëT:áâ
                    ÆzQ-eÎ:ÓV1ÁRa&ª¬±[ýª«¥éHDl¨-Âb"ÔË¨"sÂµ)þ9³vxõ¥/Ñ¡K1vVîT ¯Ç*â¬êJãº7z0ÊÇF^
                    ¢ÚZ{»ÁmÓbt?² RïXÆ~ú
                    ê2.mÛA¡yZK2xGo3@rèUÅ4ÅÒïzç¤úé¨Ï@ßÊ(Ô±hnDòRÑàÐ> ç0ÖºÁZáÜÁJ¨¢¾)§)÷jËD
                    `ò«¤$¾ïr«5w­XÆeMk1ãv3­µ·H:IjÆõÃfWr¿¦r'¡ôgi¹»Ø),QåÑÝ	Æ¼V%P~(°²ÝpX¨÷dè©ÝÈ¦ö2ö]mÐ«0)uÛ.pß=â8*¡´Êb·òId>gFet5ª0J}çÂ3J¶2ýª\ÁÎzuè°ÅsG²ÖÐÕ\5<k¸÷HäÊ¬~´Ï¿q(ßëóª·ñ{M(Ïª1qöÏy¾ Z0A^´Íñ»ÞÔU®£{ì
                    %áT©s/ÆU$s2ÏÏGoóÂ'£òµÂ¶J~Ìy:%¿
                    ;¹-
                    aZ¿ `Õ^XÍKF&±ç6/Ýó·-,ãþ«ìv"JäIoè¡ÆI£½l£*AE©Ðó>»4ÂDÑmIÊ®äc¦BØA³!ñ(RÃVm1ÚaD'j£KBõ¬xx ±Cy·O3;+V:¹9'.uN$á÷´7OñÚ(¡4xèpñÇ{Ä!e÷ÈI¼å	Éó8ý ^];ÇHåt¶2=ËN8ÉÔWÐÌ p·Á6ñ½&×b
                    Ì êÐ&öR1Ó±=þwToÚ:²à×Þ1-W%ùRc	a{=¾jI¿xäîîæðRÚL´ØÒää	 ~rÃV­ öÃ}k¨¾Ïiú$#tY[ºÛ*T½Å»öUB(_YúÈ#Uû{À^²Û¨íÞê±öçL~Q1Ø_å¡nºÏJÚ%Ø¤±B+ØsVà)°þoòNõ1.½%~×äÆc46vÌ¦G Øá0º )HÌôú´g®¯mf 0À¥r¬[2=ðøÅú.h
                    °¸öågþdÈ^ÏEC±ö	¹MB^»×#79ze<á'¥êÄ¼FÙ(¾ïsÇæîx©P2ëH.GMÛ©Ø0Ü9uw¥av§Ô"©$ôäLÞÐè¾TÁ#;ÿ¨Áòtn`2ÕÔ÷2tÅaxbÆ?ª	|Yû°,
                    Ä¹í^4ÓÀE
                    Dñü(ØÏÙÀ0­/EÊ"§o÷E´æ6©SæW1	»%#@`JU{òÇ<
                    ÝÁãÕ©
                    JyÕm9õåßÝúài;ª90ò>d¢ÎAk²´
                    ¸KWFv
                    íGU-¢ÃºZ;zCÍ9®jQûiÒÛ«¼Cm½òAÔL:ü=ðhDÎ£ï}s¾w,Ù}jè`E®[GÑ4t©)+B«<<WÅhÃÙà;Ò¥åQj6«ZD³m«tï¢$]FÏ=.kçpîûäÙ²X	¬Ã Ã±Ñ!rê¼Äë6®#&TXgò±Á²±d÷r»è0ÂÔ3¡¾dkÅXÇw@Î³Ì¡ý¡
                    m­ûØÃrq¿õhfJ¸ÑÉÓÁeEòj1ä7¬Fôlükâig._éd§nÓIe­¯YîßË%{]¶óu}Ea|rÍ7×_vBâ¨­áÜ |so·%6ÖÐÐ²ÜhÜÄú²ßé¤æE<NÍlù_ò8~°êh	óÇ³bk^üÁ$à®Ô¥x*¡ïcg+Ñh×U­µTrÐÚg,`&zHÄê+-Ùn§@UnÖHlDàbÉMAëëI³fm]ÐUùWuDf}ß;>ÓMísÄÏIR¯u öëwA0CêÒfÒ3dð°`üÎÌÅN9Nñq_Æ¾	f!¬M·<©+d?ñÓUÌ¡m8Ñ;bZµUÎÖÛ²8ýx(lç¥±}Þ»òo#^ìn¨+q3L@©JR§s ÷±e<øÇÝÈÁRÐ=JijCÌÖvÅxä(Vó¢â'
                    äèpòzd?Û°£
                    <ÖÃPÂ	øW²ùQ£G3"}úç;Û¹2²¤¦Ò0/Fîdâ>ëziíWÜ(tî`ìÐÄÿ·d¢RêÑûkbè§
                    M0e8]9ú 2,%S^£Â+Ácè:&I@Drßd37%`\ÐûÁ-bäçV÷`rìmÌùËÖèùñrúo_ðé|X.ô\Ü\@QoÔ$4uÚFøIÏbÏ»;(P@FDAWÒ2pÜbbugÌÍ}DÙH¤ GL9¬=T_Åé@°ÍTK
                    ,óJÉË§% èQ36rsÒwâ@JÌw4Ó¨òd0iÞªÇ~i{pê^Y
                    D+7ÍR¬J0²í=Mâ[!1âÚµÁ_bÀ}®¥§wçëÄ,Ê´S
                    e¡;Ène?¹ßùdýAv¹{õXÉÞc~)°³!|
                    túixÓªaD6º[´zÛ{Nö ûõÖøíìÚû0C6Öæ@3:!+Lc^}@ÇsZÎ¬þòã¥¤7ú<¦ ÚùÖÃê¾8C0ø5Y×ö?yÚñi1¦æØÆ}ØaêA2«>ýóÙÜe¢VD÷J*øõV:= áÿûÌ^IUâu^µmðZ£	Ö{ÍÖZ/ã)æy{÷4
                    àu·Ì`\ï0Î´XgWï»(Êë($¤P>rå>H¼+¬=Êjxj1âYøÉAÁ£»óÉ7DbPP¿Ç4NCH¨z ¤`¿.&êAKî|é×Ftôç«8
                    Û6ý´Üë`A5Ò2ÁLÄ7x´ýð\N±¬¶56¶ÄðÌ0º^ý|2ñq½îÈQ?èQIKªa¬
                    û
                    Jï;ðfJ¿b_àÑÔ-f
                    ÙøÔP%=&BÊèßÄÆÃ~«-25Oá*4E¨Ñ¹l3-^+ÎÚ«Òcl¿Þ ]ìèº&
                    
                    JËÌ'Á È$¾§ >#$kk¥ù
                    °c=º#ãHÁ®ÊfP>¦>Å²åæ	TiÓMå½j ·Mº÷2"e¬1À<ígEfZuDzStßÀÊR1(±SÛòØRÈ¢Û46úÊZÈå,Kw[	@gAyÄ]ÅkïëWhz©èô>7¡g5`eêÚïBÌÔk1L¼äê/(ÏÔõª½®­ |¯½æ¼p¡æå:D)ÓªBV08RpRPDôTNÈrÔA°HN=où3~wÉìÂ§¿n7ÛWûDvS±µîeÍÒðGq)Ü_­Ê·mÀ¢ÊCÕd«¬&½* h.ÐùË9_J[¸?2¹·P^2	ë	8&p·É" ]$Ju#2w*Q­çWï8sÀØä.ÍÀ$Yn·z;dÂ·	Ãü1 @bôÕ£óN¼Ùa'v@ÕÌ´YP¿g³¤ô)&5Ë1XÉ1v¸\«æo#bN¼êæ®8hõá_fÈ®Ý?A@B^+£ÕF"Ú8y)çßE6¨ä¤NúbÒ|2ªûÈSë22^vO¨,|<Å«iß(s·t}<£Í% ødê©s³Ìx×êd|s6w÷qgØ'²ª©¶[öæùìÁ7]
                    hzhC°=`²,[³1ÑñÀP¥o|^~êx¢ñ<¹»Û ÁLßÐß²*ÆÖk×éäkÐÉÒd©mÐF¡-Õöå{==_0ôZ/Ñ}gfï¯n- ã¿ML±¡Æ
                    Z¬Ò4-f¢æÍB§+8qwÅÁAÕ¬O´ê%>ïÙú³°ù>Óú±ü|::Rl`u°N7»apÛçw½4¢@9	âr=Ëka^à"NLj¡)#BÐaÖKRdtÕßDK*ÄY/b-ß.¡
                    .×´¨#X5T&	ä&ÔÝrùIí­2úi îjÑäêÞd-A¦I9á=¾1mvq¦qúX¿ãÚke©åÃ¾Ù="'âV\¹+,xóhC
                    þ
                    > ¦/N*	ÜcW¦áºg³ã«õñ;ùþxÚãG°%9ÌÖ|søÑZÃÏjKVàpK½*§õ{©N°Ö=jøêÆ§!P¸}©vÔål¡,¿HvFð>MlÙÉj
                    ÖÆ§ÌðêTÇ,t\¤¬yEc-äJû>hfqàwÝtfÈÖ@ÿÅJ2µ,-ïªvLìó5Ü¦­êR3	tû+öbL FÄ©^æ¼Ú+0­wØcW]
                    ÕóË¬[ØQZZ<Ap;¼s/§éÅ¾¶úyÁÛÉ*ü¦øpS}e^×%õYÃýõ,Ìñµ5ãG¦~2Ê*Åòò"º[ë$Ï@>,xÊØ©mUû© 3=ªÒ7H=FyBX¼OE~nÃ`Ì%~hµK¹ìH5©ú0_¥UçSe¾ùÑ÷ì/xªuÝG8ÂÐ¸Î[íÙ(KKÐ-Ò×û¨·ÅÐgùSÙÄÁ mX@¥¹%Ó´¡(*SgaãÑ=oôdÑoICÒÈR<Û)hÑi"	
                    lhÈúÄå×â3°Ð"Î/õ¤ªp§ÓÏ#>ÌwÏªËï~aôxòD¼` ïr	½éï5GÆ(ÊÃ÷N:ÕC)¶jôV53âÛÔ'Hh¿Ðþ9Äéu+$¶Y
                    dªÆ]Ò×7!ÙîóÚÎ2ò#DÀ¼ÍêZ/eáA2«W>Oê/V1í°Ö%:SÕë4G¸×Ìµ¸Uæ¹8µ´qúÈÄXÉ¡Ûj±7{ÅüH<0ÅÑLK«OÁr]kð¬U 1U/É¿cr-_óç	ò}ái'ä¸hÛlæ[¶³*½$ò\åK(0aåq(pZ¯ÃÎ´üBO
                    ÈûK,óÄ
                    m°Dê»CÄwÞ÷ér·kÍÕw÷(x$½XÞ¼8Ï_=°É 4¯XW³ñCÍ!ÊÝãèw".lØ;Z64 ¡áØwÒ4É¥è­ÎÃ©¿H! cûd/\éEâ¦-Ó]\ä~áwOÃØl*¥½L¨,,¥|·^lûäËQû±
                    G±XóW`Ì?£![²ÿ_àQÇ5aðÉq¦b ¶(I ¿Þ©ÜyX²ØÙ³ôI}ËoÊEX¤õvGvýa»-ÌæÜ\~ÄQµÝJÆÄWø¹ñ
                    }ÝÔuuÆÔ/&*¸Þ!¦ýXE
                    hYYÑÄÇÌeenÁÉ¡ÐgÉpR¾ýx¶w~ÈUÓþ	SSßJ	æ©õo\7)jÍªÿàÕ;©Ãs£Ã¢@t¡ªÈyÙ@`Õ:æ++áê¹ßôØ\P'>e¾)öØe,ì)ÿÝÚÿ
                    @Í­® êûÚ¥¡Ï4C°ÍË\ÔñÖ¹ESþç$+'°é.rÆÁ£Î¼ 1ÆAÓÑ	pÁÂÂ)Bù]x¥3Äm¤Bq(æ(~ì¨°	òÖ
                    U>2ÙÊÅpþ#/sÆMÁÕ®·Ê]¡Âèù:,j"TecÄu)^Bq^Þ?Ý}d`c²&¥ò5
                    QÙ
                    '×¦±	}é jôï7ølTKÁPÉ>!~!s$#{0Å-^©<Vëäø¾:èL RMIÌÆ¼Á,µíUéÄóþ¾ÏË©ís¢÷QÁ5
                    tGNagyZìwK×õÜökd¦^ÜØ7s:×ñYê¦«UÁ¹l<d ìRô3 Äì[Æ·Â2
                    2«âI%»xx¶	$¹HøÈf}_¾Ü%rí{B[yöäUS­í¨O"*	D±røÄQ
                    Ù,ÅæTÃSÃpÿJhÂØ^ºâýIÑF¸£{îm4×&Ó$)í¿ß]Öôk%»Án}tXv¡AÀÛf	ê{Ezmvfß>C^á`®ÂYß©Aáøá[À1v¾vZd~V9¶ÕäNkeóé$ºÜd§Tî¥	À! eRÙ¬-¢RºX¨WÙt©ÏÂuû$ñj:£Çõ¯Î§¹Ò´}/1Q$;hOrkþðUB_óÖr`0J³x¢0Ïf4}>J
                    <z¯As¤Xipê )Ñqm°Dw1T¹¤ë2£qÙÅ7v¨¤ »@
                    #UO¤BRÕqÈVD*U$GCjjÀE@GæY½
                    EÚLü3Ã²O¾æ'îåî¥\B¨B½Ò`Í^ã;;În4
                    %qÌ}.iOF.Û£úPña@¢A.ãk`W?02ñ¥04t+ÚI)a¬j¢2Pôs
                    ^=¡¯mt(AQc!#%-÷4 ßÓh;¡ÇNî:&ZA] ÝëI,ÈìOZ¼kz÷¸ð^-Õ±H~¸: ïEªPë	ò2à[<Üe"ÝÙ?\Iß:¼kÈù³pM!KçA?ùq¢S
                    RÒ@g<^HþPm/¤û9ÎÁøà&¯¾)Â±Ã,17nÍÁôµ">QÊËßÏf$ôüÎ¥á ÄôµÊRô³W¥T:n1]Çý¹Z½ÈÓþ6cf:­bziâæ5èÍRÅãÂ¬1½Þ0ä~B6üª(,M
                    ¨Ýe6ë½ÙíÁË*¸4P\Ú»rI-TÙEgøG&)@§®¯}?;£Ê@×E¦ÊÖÀ+
                    :
                    
                    "0010Óv`rB"
                     Aý aøàÑí>?Ä ¹s©	üñ¸M±y,
                    ¾ *Ð"ËÛé_"¿æ«hwøK+Ü¤ñBÖ2MÝf³´Ò~£ü¦]ÞY55¨Êà|}XÔ¼õ#'ËÐØ-FÒnOì6&íÆ5á>ÜÇB¼&êÈWõ7,¤zà©Ù7ó9Çq%2oÌó½UVÄ4¤èF:¹LhwÒûØÁÿö@ªaÄ²Æo¯ÜNÎÒÞZ*cÓXyv>]¨`<f
                    «~î0>8ó)wî` iÔXaR?ÇJd³ÓÔ\z½ôýs"ü+Ã:ÇX;­Xìa6	ã:ò'è	IBX®R³	Ôr_,x>×ÌR(&?6É{ÆèCú(l¾è/D¡Ëò4¨Á­
                    	ÿzµgåbáFÖ¹Ýp zùÀl2*¬	l"Óá§aö¡Û12Dy	]­ÌÁsª«e¹¦Ó,pl`§Èývv²&ÖAÊãtù·ºGF
                    qt Ön 
                    ~Ý´`Ò®-R«}j
                    TSáè^LÞçA¶Â.,ÐØ ¡F$¶eqr«ñ6£ÓDèÉBçnP:
                    
                    "0010Ó
                    Ð8fB"
                     l%¼Ø÷ÎRé![Ê²m?~ï!¦ÄyFôÝ;ÿZ¾
                     *±"¬À U" á¡X
                    »Íf±þßö-`mgR²;¤cÝûBiõ7ã\Ã6³×¼"}ÒúøÂ"ËÐ¸AºwÛ5ÿ~$âxt´×|'@ZéÃ},DÈkÒXÈæ±T«lqÒë§<È¥¸1Ï9+É|³ÀdoÓë~\¥Õbyc÷ÿ°ÿí.%=X]4.äõÇPïA­ÓÎWYFáIöÀøà@Ì§¼ÜÛ[aR?ÇJäy%3¼NÇòøç¤²Å&a\Gþ=!©SËÊOÇû:`Á»ð¹¸`y÷ÑôQØ|Ä9Õ¼ÕÄb8ê·ÊòvC,¦¿â	Ã='·ÎDO£;¯óµa2*Ïn"ìd¤ÍZZ^&'ãQ%Ï­¥HÊÍ 
                    MÁúÖÃ´v½ß £¦¸ÒÃÀeÒêüæwaÉÑ*%7BÍ×q1+Àq|2nÝ÷fl
                    ØÊÕ÷5ZIQ6G¹[ÂB!/ì}âò¥]Î¦ãB9:
                    
                    "0010ÈÊ
                    Á*¹B"
                     ?ßãÖ±[un'ÃÛ\%ãNÎùú¼_
                     *Ú"Õ×ô%:"É>~,Xl'¡#zféá9mÅÑ7Î$x] Ý. C%ëZÓëDúp_&B¢w¼SÇÈ^Õ^{Bqc8t¿Ä¥!ýé¶é*åÚ­|}&ïë´q	r5ûÕáÁTHÀw$géÞZ®~x¤ùZ´{6cèXÃØ
                    ´V`uäO°'$uÂrU¢QÒ¼ÓÌ\Ãµè>:-ÓéÓô0&½?=N0¸.NÃÚP=dúÊ¨&Î2v*r(>"iä«MiH©%lDØ×\,D4æEVq^­Èw·f¢èULzóâ=$Ò#<XäëxHZ¸°JÌåØú:o3¼ü_à¥Rà«%§ôP2p*©íìtpXÑeØ¦Ã{9À¼¨/:
                    
                    "0010ÏÅR)B"
                     ëF¤çì3$åcqP%H¾5xóêCËñ
                    G	 :
                    
                    	"0010#åbPB"
                     ¤ã®bm©nC{PLÇ¾àÍ^¯}[Â9	Àðþ
                
                Evidence
                
                    scaffolding on HTTPServer2
                
                Solution
                
                Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.
                
    2.  #### https://api.qa.permate.com (1)
        
        1.  ##### [Strict-Transport-Security Header Not Set](#alert-type-3) (1)
            
            1.  OPTIONS https://api.qa.permate.com/v1/auth/login
                
                Alert tags
                
                *   [OWASP\_2021\_A05](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)
                *   [OWASP\_2017\_A06](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html)
                
                Alert description
                
                HTTP Strict Transport Security (HSTS) is a web security policy mechanism whereby a web server declares that complying user agents (such as a web browser) are to interact with it using only secure HTTPS connections (i.e. HTTP layered over TLS/SSL). HSTS is an IETF standards track protocol and is specified in RFC 6797.
                
                Request
                
                Request line and header section (484 bytes)
                
                    OPTIONS https://api.qa.permate.com/v1/auth/login HTTP/1.1
                    host: api.qa.permate.com
                    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
                    Accept: */*
                    Accept-Language: en-US,en;q=0.5
                    Access-Control-Request-Method: POST
                    Access-Control-Request-Headers: content-type
                    Referer: https://qa.permate.com/
                    Origin: https://qa.permate.com
                    DNT: 1
                    Connection: keep-alive
                    Sec-Fetch-Dest: empty
                    Sec-Fetch-Mode: cors
                    Sec-Fetch-Site: same-site
                
                Request body (0 bytes)
                
                Response
                
                Status line and header section (659 bytes)
                
                    HTTP/1.1 200 OK
                    Date: Sun, 07 Jan 2024 13:17:37 GMT
                    Content-Type: text/html; charset=utf-8
                    Content-Length: 0
                    Connection: keep-alive
                    x-amzn-RequestId: 897d8054-e663-4753-b98c-e0caab7d94a2
                    Access-Control-Allow-Origin: https://qa.permate.com
                    Allow: OPTIONS, POST
                    Access-Control-Allow-Headers: content-type
                    x-amzn-Remapped-Content-Length: 0
                    x-amzn-Remapped-Connection: keep-alive
                    x-amz-apigw-id: RK6huHjsoAMED7w=
                    Vary: Origin
                    x-amzn-Remapped-Server: gunicorn
                    Access-Control-Allow-Methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
                    X-Amzn-Trace-Id: Root=1-659aa471-7351f5966b9f1cdc578040d7
                    x-amzn-Remapped-Date: Sun, 07 Jan 2024 13:17:37 GMT
                
                Response body (0 bytes)
                
                Solution
                
                Ensure that your web server, application server, load balancer, etc. is configured to enforce Strict-Transport-Security.

4.  ### Risk\=Informational, Confidence\=High (1)

    1.  #### https://api.qa.permate.com (1)

        1.  ##### [Authentication Request Identified](#alert-type-4) (1)

            1.  POST https://api.qa.permate.com/v1/auth/login

                Alert tags

                Alert description

                The given request has been identified as an authentication request. The 'Other Info' field contains a set of key=value lines which identify any relevant fields. If the request is in a context which has an Authentication Method set to "Auto-Detect" then this rule will change the authentication to match the request identified.

                Other info

                userParam=business\_email

                userValue=kien.nguyen+2@permate.com

                passwordParam=password

                referer=https://qa.permate.com/

                Request

                Request line and header section (480 bytes)

                    POST https://api.qa.permate.com/v1/auth/login HTTP/1.1
                    host: api.qa.permate.com
                    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0
                    Accept: application/json, text/plain, */*
                    Accept-Language: en-US,en;q=0.5
                    Content-Type: application/json
                    Content-Length: 71
                    Origin: https://qa.permate.com
                    DNT: 1
                    Connection: keep-alive
                    Referer: https://qa.permate.com/
                    Sec-Fetch-Dest: empty
                    Sec-Fetch-Mode: cors
                    Sec-Fetch-Site: same-site

                Request body (71 bytes)

                    {"business_email":"kien.nguyen+2@permate.com","password":"Kien1234%2w"}

                Response

                Status line and header section (520 bytes)

                    HTTP/1.1 400 Bad Request
                    Date: Sun, 07 Jan 2024 13:17:38 GMT
                    Content-Type: application/json
                    Content-Length: 45
                    Connection: keep-alive
                    x-amzn-RequestId: 5f9d4be3-f4f8-4192-af8e-abd090598016
                    Access-Control-Allow-Origin: https://qa.permate.com
                    x-amzn-Remapped-Content-Length: 45
                    x-amzn-Remapped-Connection: keep-alive
                    x-amz-apigw-id: RK6hyENXIAMEJ4A=
                    Vary: Origin
                    x-amzn-Remapped-Server: gunicorn
                    X-Amzn-Trace-Id: Root=1-659aa471-4cbada8a35adc12f3f2f66cd
                    x-amzn-Remapped-Date: Sun, 07 Jan 2024 13:17:38 GMT

                Response body (45 bytes)

                    {"errors":{"password or email":["c_c14_1"]}}

                Parameter

                    business_email

                Evidence

                    password

                Solution

                This is an informational alert rather than a vulnerability and so there is nothing to fix.


Appendix
--------

### Alert types

This section contains additional information on the types of alerts in the report.

1.  #### Content Security Policy (CSP) Header Not Set

    Source

    raised by a passive scanner ([Content Security Policy (CSP) Header Not Set](https://www.zaproxy.org/docs/alerts/10038/))

    CWE ID

    [693](https://cwe.mitre.org/data/definitions/693.html)

    WASC ID

    15

    Reference

    1.  [https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing\_Content\_Security\_Policy](https://developer.mozilla.org/en-US/docs/Web/Security/CSP/Introducing_Content_Security_Policy)
    2.  [https://cheatsheetseries.owasp.org/cheatsheets/Content\_Security\_Policy\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
    3.  [http://www.w3.org/TR/CSP/](http://www.w3.org/TR/CSP/)
    4.  [http://w3c.github.io/webappsec/specs/content-security-policy/csp-specification.dev.html](http://w3c.github.io/webappsec/specs/content-security-policy/csp-specification.dev.html)
    5.  [http://www.html5rocks.com/en/tutorials/security/content-security-policy/](http://www.html5rocks.com/en/tutorials/security/content-security-policy/)
    6.  [http://caniuse.com/#feat=contentsecuritypolicy](http://caniuse.com/#feat=contentsecuritypolicy)
    7.  [http://content-security-policy.com/](http://content-security-policy.com/)

2.  #### Cross-Domain Misconfiguration

    Source

    raised by a passive scanner ([Cross-Domain Misconfiguration](https://www.zaproxy.org/docs/alerts/10098/))

    CWE ID

    [264](https://cwe.mitre.org/data/definitions/264.html)

    WASC ID

    14

    Reference

    1.  [https://vulncat.fortify.com/en/detail?id=desc.config.dotnet.html5\_overly\_permissive\_cors\_policy](https://vulncat.fortify.com/en/detail?id=desc.config.dotnet.html5_overly_permissive_cors_policy)

3.  #### Server Leaks Version Information via "Server" HTTP Response Header Field

    Source

    raised by a passive scanner ([HTTP Server Response Header](https://www.zaproxy.org/docs/alerts/10036/))

    CWE ID

    [200](https://cwe.mitre.org/data/definitions/200.html)

    WASC ID

    13

    Reference

    1.  [http://httpd.apache.org/docs/current/mod/core.html#servertokens](http://httpd.apache.org/docs/current/mod/core.html#servertokens)
    2.  [http://msdn.microsoft.com/en-us/library/ff648552.aspx#ht\_urlscan\_007](http://msdn.microsoft.com/en-us/library/ff648552.aspx#ht_urlscan_007)
    3.  [http://blogs.msdn.com/b/varunm/archive/2013/04/23/remove-unwanted-http-response-headers.aspx](http://blogs.msdn.com/b/varunm/archive/2013/04/23/remove-unwanted-http-response-headers.aspx)
    4.  [http://www.troyhunt.com/2012/02/shhh-dont-let-your-response-headers.html](http://www.troyhunt.com/2012/02/shhh-dont-let-your-response-headers.html)

4.  #### Strict-Transport-Security Header Not Set

    Source

    raised by a passive scanner ([Strict-Transport-Security Header](https://www.zaproxy.org/docs/alerts/10035/))

    CWE ID

    [319](https://cwe.mitre.org/data/definitions/319.html)

    WASC ID

    15

    Reference

    1.  [https://cheatsheetseries.owasp.org/cheatsheets/HTTP\_Strict\_Transport\_Security\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
    2.  [https://owasp.org/www-community/Security\_Headers](https://owasp.org/www-community/Security_Headers)
    3.  [http://en.wikipedia.org/wiki/HTTP\_Strict\_Transport\_Security](http://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
    4.  [http://caniuse.com/stricttransportsecurity](http://caniuse.com/stricttransportsecurity)
    5.  [http://tools.ietf.org/html/rfc6797](http://tools.ietf.org/html/rfc6797)

5.  #### Authentication Request Identified

    Source

    raised by a passive scanner ([Authentication Request Identified](https://www.zaproxy.org/docs/alerts/10111/))

    Reference

    1.  [https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/auth-req-id/)