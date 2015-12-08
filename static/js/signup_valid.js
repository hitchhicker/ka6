$(document).ready(function(e){
	$("#signup").on("submit", function(){
		return validate_form(this);
	});
	$("#inputEmail").on("focusout", function(){
		return isValidEmail(this);
	});
	$("#inputNickName").on("focusout", function(){
  		return isValidName(this);
  	})
  	$("#inputPassword").on("focusout", function(){
  		return isValidPassword(this);
  	})
});


function validate_form(thisform)
/**
* Check all the input of the form
* 
* @param thisfrom: Form Element 
* @return boolean
*/
{
	with (thisform)
	{
		return (isValidEmail(email)
			&&isValidName(nickname)
			&&isValidPassword(password)
			&&isValidPassword(confirm)
			&&isEqual(password, confirm));
	}
}

function isNull(field)
/**
*
* @param field: Input Element
* @return boolean
*/
{
	with (field)
	{
  		var is_valid = (value != null && value.trim() != "");
		print_error(is_valid, placeholder + '为空', field);
	}
	return !is_valid;
}

function isValidPassword(password)
/**
*
* @param password: Input Element
* @return boolean
*/
{
	if (!isNull(password))
	{
		var is_valid = password.value.length >= 6;
		print_error(is_valid, "密码至少6个字符", password);
		return is_valid;	
	}
	else
	{
		return false;
	}
}

function isEqual(pw1, pw2)
/**
*
* @param pw1, pw2: Input Element
* @return boolean
*/
{
	var is_valid = pw1.value == pw2.value;
	print_error(is_valid, "两次输入密码不一致", pw2);
	return is_valid;
}

function isValidName(name)
/**
*
* @param pw1, pw2: Input Element
* @return boolean
*/
{
	is_valid = isNull(name)
	if (!isNull(name))
	{	
		var is_valid = name.value.length <= 15;
		print_error(is_valid, "昵称长度必须小于15个字符", name);
		return is_valid;
	}
	else
		return false;
}

function isValidEmail(email)
/**
*
* @param email: Input Element
* @return boolean
*/
{
	if (!isNull(email))
	{
		var pattern = /^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$/;
        is_valid = pattern.test(email.value);
        print_error(is_valid, "不是正确的邮箱格式", email);
        return is_valid;
	}
	else
		return false;
}

function print_error(isValid, errMsg, field)
/**
*
* @param isValid: boolean
* @param errMsg: string
* @param field: Input Element
* @return boolean
*/
{
	var input = $("#" + field.id)
	if (!isValid)
	{
		input.addClass("error-box");
		input.next().text(errMsg);
		// input.focus();
	}
	else
	{
		input.removeClass("error-box");
		input.next().text("");
	}
}

