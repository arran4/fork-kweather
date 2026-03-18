import re

with open("krunner/kweather_runner.cpp", "r") as f:
    data = f.read()

new_match_body = """{
    QString query = context.query().trimmed();
    QString cmd = i18nc("Command to get weather", "weather");
    QString engCmd = QStringLiteral("weather");

    QString locationStr;
    if (query.compare(cmd, Qt::CaseInsensitive) == 0 || query.compare(engCmd, Qt::CaseInsensitive) == 0) {
        locationStr = QString();
    } else if (query.startsWith(cmd + QLatin1Char(' '), Qt::CaseInsensitive)) {
        locationStr = query.mid(cmd.length() + 1).trimmed();
    } else if (query.startsWith(engCmd + QLatin1Char(' '), Qt::CaseInsensitive)) {
        locationStr = query.mid(engCmd.length() + 1).trimmed();
    } else {
        return; // Does not match exactly "weather" or "weather "
    }

    if (locationStr.isEmpty()) {"""

data = re.sub(
    r"\{\s*QString query = context\.query\(\);\s*QString cmd = i18nc\(.*if \(locationStr\.isEmpty\(\)\) \{",
    new_match_body,
    data,
    flags=re.DOTALL
)

with open("krunner/kweather_runner.cpp", "w") as f:
    f.write(data)
