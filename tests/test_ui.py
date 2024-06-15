import pytest
import time
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def dash_duo(dash_duo):
    from app.app import app  
    app.server.config['TESTING'] = True  
    dash_duo.start_server(app)
    time.sleep(3)
    return dash_duo

def test_initial_conditions(dash_duo):
    assert dash_duo.find_element('#date-picker-start'), "Date picker start should be on screen"
    assert dash_duo.find_element('#date-picker-end'), "Date picker start should be on screen"
    assert dash_duo.find_element('#choose_ticker_dropdown'), "Tickers dropdown should be on screen"
    assert dash_duo.find_element('#choose_method_dropdown'), "Methods dropdown should be on screen"

def test_tickers_dropdown_functionality(dash_duo):
    dash_duo.select_dcc_dropdown('#choose_ticker_dropdown', value='Apple')
    time.sleep(2)
    dash_duo.select_dcc_dropdown('#choose_ticker_dropdown', value='Google')
    graph = dash_duo.find_element('#stock_graph')
    assert graph.is_displayed()

def test_methods_dropdown_functionality(dash_duo):
    dash_duo.select_dcc_dropdown('#choose_method_dropdown', value='Close')
    time.sleep(2)
    dash_duo.select_dcc_dropdown('#choose_method_dropdown', value='MACD')
    dash_duo.select_dcc_dropdown('#choose_method_dropdown', value='MA')
    dash_duo.select_dcc_dropdown('#choose_method_dropdown', value='RSI')
    dash_duo.select_dcc_dropdown('#choose_method_dropdown', value='Swing')
    time.sleep(2)
    graph = dash_duo.find_element('#stock_graph')
    macd_container = dash_duo.find_element('#macd_parameters_container')
    ma_container = dash_duo.find_element('#ma_window_container')
    rsi_container = dash_duo.find_element('#rsi_window_container')
    swing_container = dash_duo.find_element('#swing_shift_container')
    assert graph.is_displayed() 
    assert macd_container.is_displayed() 
    assert ma_container.is_displayed() 
    assert rsi_container.is_displayed() 
    assert swing_container.is_displayed() 

def test_date_picker_interaction(dash_duo):
    date_picker = dash_duo.find_element('#date-picker-end input')
    date_picker.clear()
    date_picker.send_keys('2023-01-01')
    date_picker.send_keys(Keys.ENTER)
    dash_duo.wait_for_element('#stock_graph', timeout=10)
    graph = dash_duo.find_element('#stock_graph')
    assert graph.is_displayed()


def test_news_updates_on_ticker_change(dash_duo):
    dash_duo.select_dcc_dropdown('#choose_ticker_dropdown', value='Apple')
    time.sleep(2)
    dash_duo.select_dcc_dropdown('#choose_ticker_dropdown', value='Tesla')
    dash_duo.find_element('#load-news-btn').click()
    time.sleep(8)
    dash_duo.select_dcc_dropdown('#choose_ticker_filter', value='Tesla')
    time.sleep(8)
    news_text = str(dash_duo.wait_for_element('#news_list').text)
    news_container = dash_duo.find_element('#news_container')
    assert (news_container.is_displayed()) and ('(Tesla)' in news_text), "News list should be displayed, updated and contain Tesla news"



