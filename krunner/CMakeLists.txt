kcoreaddons_add_plugin(krunner_kweather SOURCES kweather_runner.cpp)
target_link_libraries(krunner_kweather KF6::Runner KF6::I18n KF6::ConfigCore KWeatherCore)
install(TARGETS krunner_kweather DESTINATION ${KDE_INSTALL_PLUGINDIR}/kf6/krunner)
