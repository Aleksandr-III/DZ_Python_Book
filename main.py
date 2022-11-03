import interface as ui
import logger as lg
import creature


lg.logging.info('Старт')
creature.init_data_base('base_phone.csv')
ui.ls_menu()