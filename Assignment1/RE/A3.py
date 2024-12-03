import re

text = """
                                </div>
                                <a href="/football/match/402568/بازی-منچستر-یونایتد-لیورپول" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>منچستر یونایتد</span></div>
                                    <div class="fixture-result-match-goals"><span class="host"></span><span> - </span><span class="guest"></span></div>
                                    <div class="fixture-result-match-guest"><span>لیورپول</span></div>
                                </a>
                                <div class="fixture-result-match-time">

                                    <span class="match-clock">18:30</span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>

</div>
<div class="widget-footer"> <a href="/football/league/3/لیگ-برتر-انگلیس/بازی-ها" >برنامه بازی های لیگ برتر انگلیس</a></div>
                </div>
            </div>



        <div class="adbox" data-id="346">
                <div style="background-color: #f5f5f5;height:300px" class="native-holder shimmer">
                    <div id="pos-slider-3545"></div>
                </div>
    </div>


            <div class="widget-holder">
                <div class="widget league schedual football" id="84">



<div class="widget-header" style="">
    <h2>

        <span style="">جدول لیگ های خارجی</span>
    </h2>
    <div class="select-options">
        <select id="stage-84">
                    <option value="902613" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902613">لیگ برتر انگلیس </option>
                    <option value="902646" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902646">بوندسلیگا آلمان </option>
                    <option value="902614" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902614">لالیگا اسپانیا </option>
                    <option value="902645" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902645">سری آ ایتالیا </option>
                    <option value="902616" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902616">لیگ یک فرانسه </option>
                    <option value="902649" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902649">لیگ برتر پرتغال </option>
                    <option value="902631" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902631">اردیویسه هلند </option>
                    <option value="902659" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902659">لیگ حرفه‌ای عربستان </option>
                    <option value="902630" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902630">ژوپیرلیگ بلژیک </option>
                    <option value="902624" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902624">چمپیونشیپ انگلیس </option>
                    <option value="902629" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902629">لیگ برتر روسیه </option>
                    <option value="902344" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902344">لیگ برتر امارات </option>
                    <option value="902658" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902658">سوپرلیگ ترکیه </option>
                    <option value="902570" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902570">سری آ برزیل </option>
                    <option value="902571" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902571">سوپرلیگ آرژانتین </option>
                    <option value="902656" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902656">لیگ ستارگان قطر </option>
                    <option value="902549" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902549">کی لیگ کره جنوبی </option>
                    <option value="902548" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902548">جی لیگ ژاپن </option>
                    <option value="902632" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902632">پریمیرلیگ اسکاتلند </option>
                    <option value="902633" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902633">سوپرلیگ سوئیس </option>
                    <option value="902634" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902634">بوندسلیگا اتریش </option>
                    <option value="902640" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902640">لیگ برتر کرواسی </option>
                    <option value="902641" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902641">سوپرلیگ دانمارک </option>
                    <option value="902642" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902642">لیگ برتر اوکراین </option>
                    <option value="902396" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902396">سوپرلیگ یونان </option>
                    <option value="902650" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902650">لیگ برتر قبرس </option>
                    <option value="902643" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902643">لیگ برتر لهستان </option>
                    <option value="902625" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902625">لیگ برتر جمهوری چک </option>
                    <option value="902623" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902623">سوپرلیگ صربستان </option>
                    <option value="902551" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902551">کنفرانس شرق MLS </option>
                    <option value="902552" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/84/league/902552">کنفرانس غرب MLS </option>
        </select>

    </div>
</div>
<div class="widget-body">

    <div class="widget-table">
        <div class="widget-subtitle" style="background-color:#4285f4"><h3>جدول لیگ برتر انگلیس</h3></div>
        <div class="table-holder">
            <table class=" league-standing widget-standing">
                <caption>جدول لیگ برتر انگلیس</caption>
                <thead>
                    <tr>
                        <th scope="col">رتبه</th>
                        <th scope="col">تيم</th>
                        <th scope="col">بازی</th>
                        <th scope="col">امتياز</th>
                    </tr>
                </thead>
                <tbody>
                            <tr>
                                <td>1</td>
                                <td scope="row"><a href="/football/team/84/منچسترسیتی"> منچسترسیتی</a></td>
                                <td>2</td>
                                <td>6</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td scope="row"><a href="/football/team/413/برایتون"> برایتون</a></td>
                                <td>2</td>
                                <td>6</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td scope="row"><a href="/football/team/87/آرسنال"> آرسنال</a></td>
                                <td>2</td>
                                <td>6</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td scope="row"><a href="/football/team/83/لیورپول"> لیورپول</a></td>
                                <td>2</td>
                                <td>6</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td scope="row"><a href="/football/team/86/تاتنهام"> تاتنهام</a></td>
                                <td>2</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td scope="row"><a href="/football/team/340/ناتینگهام-فارست"> ناتینگهام فارست</a></td>
                                <td>2</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td scope="row"><a href="/football/team/274/نیوکسل"> نیوکسل</a></td>
                                <td>2</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td scope="row"><a href="/football/team/81/چلسی"> چلسی</a></td>
                                <td>2</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td scope="row"><a href="/football/team/96/وستهم"> وستهم</a></td>
                                <td>2</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>10</td>
                                <td scope="row"><a href="/football/team/94/فولام"> فولام</a></td>
                                <td>2</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td scope="row"><a href="/football/team/82/منچستر-یونایتد"> منچستر یونایتد</a></td>
                                <td>2</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td scope="row"><a href="/football/team/85/استون-ویلا"> استون ویلا</a></td>
                                <td>2</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>13</td>
                                <td scope="row"><a href="/football/team/900810/برنتفورد"> برنتفورد</a></td>
                                <td>2</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>14</td>
                                <td scope="row"><a href="/football/team/901069/بورنموث"> بورنموث</a></td>
                                <td>2</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td>15</td>
                                <td scope="row"><a href="/football/team/332/لسترسیتی"> لسترسیتی</a></td>
                                <td>2</td>
                                <td>1</td>
                            </tr>
                            <tr>
                                <td>16</td>
                                <td scope="row"><a href="/football/team/900683/ساوتهمپتون"> ساوتهمپتون</a></td>
                                <td>2</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>17</td>
                                <td scope="row"><a href="/football/team/900872/کریستال-پالاس"> کریستال پالاس</a></td>
                                <td>2</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>18</td>
                                <td scope="row"><a href="/football/team/331/ایپسویچ"> ایپسویچ</a></td>
                                <td>2</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>19</td>
                                <td scope="row"><a href="/football/team/92/ولورهمپتون"> ولورهمپتون</a></td>
                                <td>2</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>20</td>
                                <td scope="row"><a href="/football/team/93/اورتون"> اورتون</a></td>
                                <td>2</td>
                                <td>0</td>
                            </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
<div class="widget-footer"> <a href="/football/league/3/لیگ-برتر-انگلیس" >جدول کامل لیگ برتر انگلیس</a></div>
                </div>
            </div>



            <div class="widget-holder">
                <div class="widget league schedual football" id="117">


<div class="widget-header">
    <h2>جام‌های حذفی باشگاهی</h2>
    <div class="select-options">
        <select id="league-117">
                    <option value="22" selected="selected">جام حذفی ایران </option>
                    <option value="14">جام حذفی انگلیس </option>
                    <option value="13">جام اتحادیه انگلیس </option>
                    <option value="15">جام حذفی اسپانیا </option>
                    <option value="11">جام حذفی آلمان </option>
                    <option value="19">جام حذفی ایتالیا </option>
                    <option value="8">جام حذفی فرانسه </option>
        </select>
        <select id="stage-117">
                    <option style='display: block' value="902503" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902503" data-league-default-stage="False">مرحله دوم </option>
                    <option style='display: none' value="902480" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902480" data-league-default-stage="False">مرحله اول </option>
                    <option style='display: none' value="902675" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902675" data-league-default-stage="False">مرحله اول </option>
                    <option style='display: none' value="902486" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902486" data-league-default-stage="False">یک سی و دوم نهایی </option>
                    <option style='display: none' value="902677" data-league="11" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902677" data-league-default-stage="True">یک سی و دوم نهایی </option>
                    <option style='display: none' value="902673" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902673" data-league-default-stage="False">یک سی و دوم نهایی </option>
                    <option style='display: none' value="902520" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902520" data-league-default-stage="False">یک سی و دوم نهایی </option>
                    <option style='display: block' value="902522" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902522" data-league-default-stage="False">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902483" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902483" data-league-default-stage="False">مرحله دوم </option>
                    <option style='display: none' value="902692" data-league="13" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902692" data-league-default-stage="True">مرحله دوم </option>
                    <option style='display: none' value="902505" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902505" data-league-default-stage="False">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902693" data-league="19" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902693" data-league-default-stage="True">یک شانزدهم نهایی </option>
                    <option style='display: none' value="902525" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902525" data-league-default-stage="False">یک شانزدهم نهایی </option>
                    <option style='display: block' value="902567" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902567" data-league-default-stage="False">یک هشتم نهایی </option>
                    <option style='display: none' value="902497" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902497" data-league-default-stage="False">مرحله سوم </option>
                    <option style='display: none' value="902523" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902523" data-league-default-stage="False">یک هشتم نهایی </option>
                    <option style='display: none' value="902538" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902538" data-league-default-stage="False">یک هشتم نهایی </option>
                    <option style='display: block' value="902593" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902593" data-league-default-stage="False">یک چهارم نهایی </option>
                    <option style='display: none' value="902524" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902524" data-league-default-stage="False">مرحله چهارم </option>
                    <option style='display: none' value="902530" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902530" data-league-default-stage="False">یک چهارم نهایی </option>
                    <option style='display: none' value="902547" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902547" data-league-default-stage="False">یک چهارم نهایی </option>
                    <option style='display: block' value="902604" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902604" data-league-default-stage="False">نیمه نهایی </option>
                    <option style='display: none' value="902537" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902537" data-league-default-stage="False">مرحله پنجم </option>
                    <option style='display: none' value="902535" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902535" data-league-default-stage="False">نیمه نهایی </option>
                    <option style='display: none' value="902563" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902563" data-league-default-stage="False">نیمه نهایی </option>
                    <option style='display: block' value="902612" selected="selected" data-league="22" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902612" data-league-default-stage="True">فینال </option>
                    <option style='display: none' value="902557" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902557" data-league-default-stage="False">یک چهارم نهایی </option>
                    <option style='display: none' value="902558" data-league="15" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902558" data-league-default-stage="True">فینال </option>
                    <option style='display: none' value="902580" data-league="8" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902580" data-league-default-stage="True">فینال </option>
                    <option style='display: none' value="902568" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902568" data-league-default-stage="False">نیمه نهایی </option>
                    <option style='display: none' value="902588" data-league="14" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/117/multiple-league/902588" data-league-default-stage="True">فینال </option>
        </select>
    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:600px">
        <div class="scroll-list-content">
            <div class="widget-subtitle" style="background-color:#4285f4"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>پنج شنبه 31 خرداد</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/402540/بازی-مس-رفسنجان-سپاهان"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>

                                </div>
                                 <a href="/football/match/402540/بازی-مس-رفسنجان-سپاهان" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>مس رفسنجان</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">0</span><span> - </span><span class="guest">2</span></div>
                                    <div class="fixture-result-match-guest"><span>سپاهان</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/345941/خلاصه-بازی-مس-رفسنجان-0-سپاهان-2"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>

</div>
<div class="widget-footer"> <a href="/football/playoffs/22/جام-حذفی-ایران">نمودار جام حذفی ایران</a></div>
                </div>
            </div>
            <div class="widget-holder">
                <div class="widget multi-sport league" id="136">

<div class="widget-header">
    <h2>جام ملت‌ها</h2>
</div>
<div class="widget-body">
    <ul class="nav nav-tabs vrz-tab" id="multiSportLeagueTab#136" role="tablist">

                <li role="tab" class="nav-item">
                    <a href="#tab_136_1-tab-content" id="tab_136_1-tab" data-toggle="tab" aria-controls="tab_136_1" class="nav-link active">اروپا</a>
                </li>
                <li role="tab" class="nav-item">
                    <a href="#tab_136_2-tab-content" id="tab_136_2-tab" data-toggle="tab" aria-controls="tab_136_2" class="nav-link">آسیا</a>
                </li>
                <li role="tab" class="nav-item">
                    <a href="#tab_136_3-tab-content" id="tab_136_3-tab" data-toggle="tab" aria-controls="tab_136_3" class="nav-link">آمریکای جنوبی</a>
                </li>
    </ul>
    <div class="tab-content" id="multiSportLeagueTabContentb#136">
            <div id="tab_136_1-tab-content" role="tabpanel" aria-labelledby="tab_136_1-tab" class="tab-pane fade football tab_136_1 active show">



<div class="widget-header" style="">
    <h2>

        <span style=""></span>
    </h2>
    <div class="select-options">
        <select id="stage-136">
                    <option value="902489" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902489">گروه A </option>
                    <option value="902490" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902490">گروه B </option>
                    <option value="902491" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902491">گروه C </option>
                    <option value="902492" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902492">گروه D </option>
                    <option value="902493" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902493">گروه E </option>
                    <option value="902494" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902494">گروه F </option>
                    <option value="902622" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902622">یک هشتم نهایی </option>
                    <option value="902644" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902644">یک چهارم نهایی </option>
                    <option value="902647" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902647">نیمه نهایی </option>
                    <option value="902652" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902652">فینال </option>
        </select>

    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#799441"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>یکشنبه 24 تیر</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/410074/بازی-اسپانیا-انگلیس"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>

                                </div>
                                <a href="/football/match/410074/بازی-اسپانیا-انگلیس" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اسپانیا</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">2</span><span> - </span><span class="guest">1</span></div>
                                    <div class="fixture-result-match-guest"><span>انگلیس</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/347555/خلاصه-بازی-اسپانیا-2-انگلیس-1-گزارش-اختصاصی"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>

</div>
<div class="widget-footer"> <a href="https://www.varzesh3.com/football/%D8%AC%D8%A7%D9%85-%D9%85%D9%84%D8%AA-%D9%87%D8%A7%DB%8C-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7-2024#playoff" >نمودار حذفی جام ملت های اروپا</a></div>
            </div>
            <div id="tab_136_2-tab-content" role="tabpanel" aria-labelledby="tab_136_2-tab" class="tab-pane fade football tab_136_2">



<div class="widget-header" style="">
    <h2>

        <span style=""></span>
    </h2>
    <div class="select-options">
        <select id="stage-136">
                    <option value="902307" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902307">گروه A </option>
                    <option value="902308" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902308">گروه B </option>
                    <option value="902309" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902309">گروه C </option>
                    <option value="902310" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902310">گروه D </option>
                    <option value="902311" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902311">گروه E </option>
                    <option value="902312" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902312">گروه F </option>
                    <option value="902531" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902531">یک هشتم نهایی </option>
                    <option value="902539" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902539">یک چهارم نهایی </option>
                    <option value="902540" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902540">نیمه نهایی </option>
                    <option value="902543" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902543">فینال </option>
        </select>

    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#799441"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>شنبه 21 بهمن</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/399893/بازی-اردن-قطر"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>

                                </div>
                                <a href="/football/match/399893/بازی-اردن-قطر" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>اردن</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">3</span></div>
                                    <div class="fixture-result-match-guest"><span>قطر</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/324357/خلاصه-بازی-اردن-1-قطر-3"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>

</div>
<div class="widget-footer"> <a href="/football/league/31/جام-ملت-های-آسیا/نمودار-حذفی" >نمودار حذفی جام ملت های آسیا</a></div>
            </div>
            <div id="tab_136_3-tab-content" role="tabpanel" aria-labelledby="tab_136_3-tab" class="tab-pane fade football tab_136_3">



<div class="widget-header" style="">
    <h2>

        <span style=""></span>
    </h2>
    <div class="select-options">
        <select id="stage-136">
                    <option value="902498" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902498">گروه A </option>
                    <option value="902499" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902499">گروه B </option>
                    <option value="902500" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902500">گروه C </option>
                    <option value="902501" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902501">گروه D </option>
                    <option value="902639" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902639">یک چهارم نهایی </option>
                    <option value="902648" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902648">نیمه نهایی </option>
                    <option value="902654" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902654">رده بندی </option>
                    <option value="902653" selected="selected" data-api="https://web-api.varzesh3.com/v1.0/football/widgets/136/league/902653">فینال </option>
        </select>

    </div>
</div>
<div class="widget-body">
    <div class="scrollable-box" style="max-height:auto">
        <div class="scroll-list-content">
             <div class="widget-subtitle" style="background-color:#799441"><h3>فینال</h3></div>
            <div class="widget-schedual">
                        <div class="date-seprator"><h4>دوشنبه 25 تیر</h4></div>
                            <div class="fixture-result-match even">
                                <div class="fixture-result-match-detail">
                                    <a href="/football/match/410123/بازی-آرژانتین-کلمبیا"> <img alt="جزئیات" width="17" height="17" src="https://static.varzesh3.com/img/icons/info-icon.svg?w=17" /></a>

                                </div>
                                <a href="/football/match/410123/بازی-آرژانتین-کلمبیا" class="fixture-result-match-teams">
                                    <div class="fixture-result-match-host"><span>آرژانتین</span></div>
                                    <div class="fixture-result-match-goals"><span class="host">1</span><span> - </span><span class="guest">0</span></div>
                                    <div class="fixture-result-match-guest"><span>کلمبیا</span></div>
                                </a>
                                <div class="fixture-result-match-time">
                                    <a target="_blank" href="https://video.varzesh3.com/video/347571/خلاصه-بازی-آرژانتین-1-کلمبیا-0-گزارش-اختصاصی"> <img alt="ویدیو" width="17" height="17" src="https://static.varzesh3.com/img/icons/video-link.svg?w=17" /></a>
                                    <span class="match-clock"></span>
                                    <span class="match-status"></span>
                                </div>
                            </div>
            </div>
        </div>
    </div>

</div>
<div class="widget-footer"> <a href="/football/league/40/کوپا-آمریکا/نمودار-حذفی" >نمودار حذفی کوپا آمریکا</a></div>
            </div>
    </div>
</div>
                </div>
            </div>

                </div>
            </div>
        </div>
        <div class="left-side-ad-col ">
            <div class="side-banner-zone tb-holder widgets-parent-col">
                <div class="forfix">

        <div class="adbox" data-id="2840">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2840" rel="nofollow"
                    style="background-color: #f5f5f5;height:400px">
                        <img class="adimage" id="img-2840" src="https://static.varzesh3.com/img/blank.png"
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/08/27/B/1ahiha5d.gif"
                                                        width="160"
                                                        height="400" alt="بیمه دات کام" />
                </a>
    </div>


        <div class="adbox" data-id="5018">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/5018" rel="nofollow"
                    style="background-color: #f5f5f5;height:300px">
                        <img class="adimage" id="img-5018" src="https://static.varzesh3.com/img/blank.png"
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/08/14/C/kbrkifpm.jpg"
                                                        width="160"
                                                        height="300" alt="فودرو" />
                </a>
    </div>


        <div class="adbox" data-id="2542">
                <a class="adlink vrz-lazy shimmer" target="_blank" href="https://biz.varzesh3.com/events/click/2542" rel="nofollow"
                    style="background-color: #f5f5f5;height:300px">
                        <img class="adimage" id="img-2542" src="https://static.varzesh3.com/img/blank.png"
                                                        data-origin="https://biz-cdn.varzesh3.com/banners/2024/08/24/C/hsrf4wkd.gif"
                                                        width="160"
                                                        height="300" alt="افرانت " />
                </a>
    </div>

                </div>
            </div>
        </div>
    </div>
</div>

        </main>
    </section>

<footer>
    <div class="allfooter">
        <div class="container">
            <div class="allfooter-menus">
                <div class="row">
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="راهنما" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/uqsoneco.svg?w=20" />
                                            راهنما
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/app">دانلود اپلیکیشن</a></li>
                                            <li><a href="https://www.varzesh3.com/contact">ارتباط با ما</a></li>
                                            <li><a href="https://www.varzesh3.com/advertisement">تبلیغات</a></li>
                                            <li><a href="https://www.varzesh3.com/about">درباره ما</a></li>
                                            <li><a href="https://www.varzesh3.com/developer-tools">ابزار توسعه دهندگان</a></li>
                                            <li><a href="https://www.varzesh3.com/careers">فرصت های شغلی</a></li>
                                            <li><a href="https://www.varzesh3.com/policy">قوانین و مقررات</a></li>
                                            <li><a href="https://www.varzesh3.com/dmca">DMCA</a></li>
                                            <li><a href="https://www.varzesh3.com/bulletins">آگهی دولتی</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سرویس ها" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/3q33ppav.svg?w=20" />
                                            سرویس ها
                                        </span>
                                    </li>
                                            <li><a href="https://video.varzesh3.com/freereporter">سوژه‌های ورزشی شما</a></li>
                                            <li><a href="https://www.varzesh3.com/news">اخبار ورزشی</a></li>
                                            <li><a href="https://www.varzesh3.com/podcast">پادکست</a></li>
                                            <li><a href="https://www.varzesh3.com/leagues">لیگ ها و رقابت ها</a></li>
                                            <li><a href="https://video.varzesh3.com/">ویدئو</a></li>
                                            <li><a href="https://www.varzesh3.com/newspaper">روزنامه</a></li>
                                            <li><a href="https://www.varzesh3.com/livescore">نتایج زنده</a></li>
                                            <li><a href="https://www.anten.ir/">آنتن</a></li>
                                            <li><a href="https://pishbini.varzesh3.com/">پیش بینی</a></li>
                                            <li><a href="https://www.varzesh3.com/پخش-زنده">پخش زنده</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="تیم های داخلی" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/4q4ntaac.svg?w=20" />
                                            تیم های داخلی
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/team/4/%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84">استقلال</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/6/%D9%BE%D8%B1%D8%B3%D9%BE%D9%88%D9%84%DB%8C%D8%B3">پرسپولیس</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/18/%D8%AA%D8%B1%D8%A7%DA%A9%D8%AA%D9%88%D8%B1">تراکتور</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/1/%D8%B0%D9%88%D8%A8-%D8%A7%D9%93%D9%87%D9%86">ذوب آهن</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/10/%D8%B3%D9%BE%D8%A7%D9%87%D8%A7%D9%86">سپاهان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/21/%D8%B5%D9%86%D8%B9%D8%AA-%D9%86%D9%81%D8%AA-%D8%A7%D9%93%D8%A8%D8%A7%D8%AF%D8%A7%D9%86">صنعت نفت آبادان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/488/%D8%A7%D8%B3%D8%AA%D9%82%D9%84%D8%A7%D9%84-%D8%AE%D9%88%D8%B2%D8%B3%D8%AA%D8%A7%D9%86">استقلال خوزستان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/9/%D9%81%D9%88%D9%84%D8%A7%D8%AF">فولاد</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/37/%D9%86%D8%B3%D8%A7%D8%AC%DB%8C-%D9%85%D8%A7%D8%B2%D9%86%D8%AF%D8%B1%D8%A7%D9%86">نساجی مازندران</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/14/%D9%85%D9%84%D9%88%D8%A7%D9%86">ملوان</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="تیم های خارجی" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/nupvsdov.svg?w=20" />
                                            تیم های خارجی
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/team/68/%D8%A7%D9%93%D8%AB-%D9%85%DB%8C%D9%84%D8%A7%D9%86">آث میلان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/63/%D8%A7%DB%8C%D9%86%D8%AA%D8%B1">اینتر میلان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/101/%D8%A8%D8%A7%D8%B1%D8%B3%D9%84%D9%88%D9%86%D8%A7">بارسلونا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/145/%D9%BE%D8%A7%D8%B1%DB%8C-%D8%B3%D9%86-%DA%98%D8%B1%D9%85%D9%86">پاری سن ژرمن</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/81/%DA%86%D9%84%D8%B3%DB%8C">چلسی</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/102/%D8%B1%D9%8A%D9%94%D8%A7%D9%84-%D9%85%D8%A7%D8%AF%D8%B1%DB%8C%D8%AF">رئال مادرید</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/83/%D9%84%DB%8C%D9%88%D8%B1%D9%BE%D9%88%D9%84">لیورپول</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/82/%D9%85%D9%86%DA%86%D8%B3%D8%AA%D8%B1%DB%8C%D9%88%D9%86%D8%A7%DB%8C%D8%AA%D8%AF">منچستریونایتد</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/62/%DB%8C%D9%88%D9%88%D9%86%D8%AA%D9%88%D8%B3">یوونتوس</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/123/%D8%A8%D8%A7%DB%8C%D8%B1%D9%86-%D9%85%D9%88%D9%86%DB%8C%D8%AE">بایرن مونیخ</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>

                                            لیگ های پرطرفدار
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/league/6/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86">جدول لیگ برتر ایران (خلیج فارس)</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/24/%D9%84%DB%8C%DA%AF-%D8%A7%D9%93%D8%B2%D8%A7%D8%AF%DA%AF%D8%A7%D9%86">لیگ آزادگان</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3">لیگ برتر انگلیس</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/2/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7">لالیگا اسپانیا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/4/%D8%B3%D8%B1%DB%8C-%D8%A7%D9%93-%D8%A7%DB%8C%D8%AA%D8%A7%D9%84%DB%8C%D8%A7">سری آ ایتالیا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/25/%D9%84%DB%8C%DA%AF-%D9%82%D9%87%D8%B1%D9%85%D8%A7%D9%86%D8%A7%D9%86-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7">لیگ قهرمانان اروپا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/league/26/%D9%84%DB%8C%DA%AF-%D9%86%D8%AE%D8%A8%DA%AF%D8%A7%D9%86-%D8%A7%D9%93%D8%B3%DB%8C%D8%A7/%D9%86%D9%85%D9%88%D8%AF%D8%A7%D8%B1-%D8%AD%D8%B0%D9%81%DB%8C">لیگ نخبگان آسیا</a></li>
                                            <li><a href="https://www.varzesh3.com/futsal/league/27/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D9%81%D9%88%D8%AA%D8%B3%D8%A7%D9%84">لیگ برتر فوتسال</a></li>
                                </ul>
                            </div>
                            <div class="col-6 col-md-2">
                                <ul class="footermenu">
                                    <li>
                                        <span>
                                            <img alt="سایر" width="20" height="20" src="https://match-cdn.varzesh3.com/footer-menu/2022/03/27/B/3szclmgh.svg?w=20" />
                                            سایر
                                        </span>
                                    </li>
                                            <li><a href="https://www.varzesh3.com/football/league/31/%D8%AC%D8%A7%D9%85-%D9%85%D9%84%D8%AA-%D9%87%D8%A7%DB%8C-%D8%A7%D9%93%D8%B3%DB%8C%D8%A7">جام ملت های آسیا</a></li>
                                            <li><a href="https://www.varzesh3.com/%D8%A7%D9%84%D9%85%D9%BE%DB%8C%DA%A9-2024">المپیک 2024 پاریس</a></li>
                                            <li><a href="https://www.varzesh3.com/%D8%A8%D8%A7%D8%B2%DB%8C-%D9%87%D8%A7%DB%8C-%D8%A2%D8%B3%DB%8C%D8%A7%DB%8C%DB%8C-%D9%87%D8%A7%D9%86%DA%AF%DA%98%D9%88">بازی‌های آسیایی هانگژو</a></li>
                                            <li><a href="https://www.varzesh3.com/football/world-cup/qatar-2022">جام جهانی 2022 قطر</a></li>
                                            <li><a href="https://www.varzesh3.com/football/fifa-ranking">رنکینگ فیفا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/transfers/euro/%D9%86%D9%82%D9%84-%D9%88-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7">نقل و انتقالات اروپا</a></li>
                                            <li><a href="https://www.varzesh3.com/football/transfers/iran/%D9%86%D9%82%D9%84-%D9%88-%D8%A7%D9%86%D8%AA%D9%82%D8%A7%D9%84%D8%A7%D8%AA-%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1">نقل و انتقالات ایران</a></li>
                                            <li><a href="https://www.varzesh3.com/football/team/87/%D8%A7%D9%93%D8%B1%D8%B3%D9%86%D8%A7%D9%84">آرسنال</a></li>
                                </ul>
                            </div>
                </div>
            </div>
            <div class="allfooter-copy">
                <div class="footerlogo"><span class="footer-logo-holder"><img alt="ورزش سه" width="20" height="20" src="https://static.varzesh3.com/img/shared/footer/logo.svg?w=20" /></span><span>ورزش سه</span></div>
                <div class="copyright" data-nosnippet>تمام حقوق مادی و معنوی این سایت متعلق به ورزش سه می باشد. شما می توانید از سایت ورزش سه در صورت پذیرش موافقت نامه کاربری استفاده نمایید.</div>
                <div class="socials">
                    <a target="_blank" rel="noopener noreferrer" href="https://facebook.com/varzesh3"> <img alt="فیس بوک" width="8" height="15" src="https://static.varzesh3.com/img/shared/footer/social/facebook.svg?w=8" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@Varzesh3."> <img alt="یوتیوب" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/youtube.svg?w=15" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://twitter.com/varzesh3"><img alt="توییتر" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/twitter.svg?w=15" /> </a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.instagram.com/varzesh3"><img alt="اینستاگرام" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/instagram.svg?w=15" /></a>
                    <a target="_blank" rel="noopener noreferrer" href="https://t.me/varzesh3"><img alt="تلگرام" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/telegram.svg?w=15" /> </a>
                    <a target="_blank" rel="noopener noreferrer" href="https://www.varzesh3.com/rss/list"><img alt="خبرخوان" width="15" height="15" src="https://static.varzesh3.com/img/shared/footer/social/rss.svg?w=15" /></a>
                </div>
            </div>
        </div>
    </div>
</footer>



<div class="searchbox" data-search-url="https://search-api.varzesh3.com/v1.0/query?q=">
    <form id="vrz-search-form" method="GET" role="search" autocomplete="off" action="/search">
        <div class="input-holder">
            <input id="main-search" class="search" type="search" name="q" placeholder="جستجوی اخبار، تیم‌ها، بازیکنان، ویدیوهای ورزشی …" />
            <span class="close-search">
                <img alt="close" src="https://static.varzesh3.com/img/icons/close-icon.svg" />
            </span>
        </div>
    </form>
</div>

<div class="search-ajax-result">
    <div id="search-result-tags tagbox ">
        <div class="search-content-type-title">
            برچسب ها
        </div>
        <div class="result-box tags-res tags"></div>
    </div>
    <div id="search-result-news">
        <div class="search-content-type-title">
            اخبار
        </div>
        <div class="result-box  news-res row"></div>
    </div>
    <div id="search-result-videos">
        <div class="search-content-type-title">
            ویدیوها
        </div>
        <div class="result-box  videos-res row"></div>
    </div>
    <div class="see-all">
        مشاهده همه نتایج
    </div>
</div>
    <div class="dark-shadow"></div>
    <span id="gotop"></span>
    <div id="alertModal" class="modal fade alerts-show" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" fill="#90A4AE" fill-rule="evenodd" />
                    </svg>

                </button>
                <div class="modal-header"></div>
                <div class="modal-body"></div>
"""
# Define the regex pattern for both id and class attributes
pattern = r'(?:id|class)\s*=\s*["\']([^"\']+)["\']'

# Find all matches in the text
matches = re.findall(pattern, text)

# Print results
for match in matches:
    print(match)
