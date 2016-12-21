Feature: Compute factorial
    In order to play with Lettuce
    As beginners
    We'll implement factorial

    Scenario: Login website and check pages
        When Navigate to /
        Then See 注册 in webpage
        Then See 登录 in webpage

        Given I have account username: <username>, password: <password>
        When Navigate to /accounts/login/
        Then Login with website account
        Then See user-bar of website account

        When Navigate to /
        Then See user-bar of website account
        When Navigate to /accounts/login/
        Then See user-bar of website account
        When Navigate to /accounts/register/
        Then See user-bar of website account

        When Navigate to /about/
        Then See title 关于我们
        Then See 关于我们 in webpage

        When Navigate to /contact/
        Then See title 联系我们
        Then See 联系我们 in webpage

        When Navigate to /privacy/
        Then See title 隐私条款
        Then See 隐私条款 in webpage

        Then Logout website

    Examples:
        | username | password |

    Scenario: Register website account and do login
        When Navigate to /
        Then See 注册 in webpage
        Then See 登录 in webpage

        Given Create a random account
        When Navigate to /accounts/register/
        Then See title 注册
        Then Register with website account
        Then See user-bar of website account

        When Logout website
        Then See title 登录

        When Navigate to /
        Then See 注册 in webpage
        Then See 登录 in webpage

        When Navigate to /accounts/login/
        Then See title 登录
        Then Login with website account
        Then See user-bar of website account

        Then Logout website
