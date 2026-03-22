# SPDX-FileCopyrightText: 2024 The KWeather Authors
# SPDX-License-Identifier: GPL-2.0-or-later

kcoreaddons_add_plugin(krunner_kweather SOURCES kweather_runner.cpp INSTALL_NAMESPACE "kf6/krunner")
target_link_libraries(krunner_kweather KF6::Runner KF6::I18n KF6::ConfigCore KWeatherCore Qt6::Network Qt6::Gui Qt6::Core)
