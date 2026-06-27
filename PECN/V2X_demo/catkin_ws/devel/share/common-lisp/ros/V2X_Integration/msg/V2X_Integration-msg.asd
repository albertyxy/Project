
(cl:in-package :asdf)

(defsystem "V2X_Integration-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BSM" :depends-on ("_package_BSM"))
    (:file "_package_BSM" :depends-on ("_package"))
    (:file "ESP_21_Msg" :depends-on ("_package_ESP_21_Msg"))
    (:file "_package_ESP_21_Msg" :depends-on ("_package"))
    (:file "FB_05_Msg" :depends-on ("_package_FB_05_Msg"))
    (:file "_package_FB_05_Msg" :depends-on ("_package"))
    (:file "SARA_06_Msg" :depends-on ("_package_SARA_06_Msg"))
    (:file "_package_SARA_06_Msg" :depends-on ("_package"))
    (:file "V2X_Warning" :depends-on ("_package_V2X_Warning"))
    (:file "_package_V2X_Warning" :depends-on ("_package"))
  ))