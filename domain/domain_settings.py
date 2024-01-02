from dataclasses import dataclass

@dataclass
class metricDetailsType:
      light_level_shown: bool
      noice_level_shown: bool


@dataclass
class settingsDetailsType:
      metric: metricDetailsType 