from utils import cisla_do_slov
import yaml


def main():
    with open("config.yaml", "r", encoding="utf-8") as f:
        conf: dict[str] = yaml.safe_load(f.read())
    print(cisla_do_slov(conf.get("input")))


if __name__ == '__main__':
    main()
